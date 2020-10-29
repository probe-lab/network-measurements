import os
import toml
import random
import string
import logging
from collections import defaultdict
# custom modules
from . import s3_api


class Observatory(object):

    def __init__(self):
        self.MAX_INSTANCES = 20
        self.experiment_id = self.generate_id(10)
        self.available_regions = s3_api.get_regions()
        self.available_azs = s3_api.get_azones(self.available_regions)

    @staticmethod
    def generate_id(length):
        """
        Generates an ID for the experiment

        :param str length:
        """
        letters_and_digits = string.ascii_letters + string.digits
        result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
        return result_str

    def validate_ec2_servers_number(self, instances_per_az):
        """
        Validates if the number of desired servers is valid

        :param instances_per_az: the requested number of instances per availability zone
        :type instances_per_az: int
        :return: True/False depending on whether the requested number is valid
        :rtype: bool
        """
        valid = False
        try:
            requested_number = int(instances_per_az)
            if requested_number > 0 and requested_number <= self.MAX_INSTANCES:
                valid = True
            else:
                logging.error("You cannot request less than 1 or "
                              "more than {} server instances per availability zone.".format(self.MAX_INSTANCES))
        except ValueError as e:
            logging.error("The 'instances_per_az' parameter in the .toml manifest file is not a valid integer.")

        return valid
    
    def validate_az_number(self, availability_zones, requested_regions):
        """
        Validates if the number of desired availability zones is valid for the requested regions.

        :param instances_per_az: the requested number of availability zones
        :type instances_per_az: int
        :poram requested_regions: the list of regions that the user requested
        :type requested_regions: list
        :return: True/False depending on whether the requested number is valid
        :rtype: bool
        """
        valid = True
        if availability_zones < 1:
            logging.error("You cannot request less than 1 availability zones...")
            valid = False
            
        for region in requested_regions:
            if len(self.available_azs[region]) < availability_zones:
                logging.error("The maximum number of availability zones "
                              "for region {} is {}".format(region, len(self.available_azs[region])))
                logging.error("The requested number of availability zones cannot be satisfied...")
                valid = False
                break
        return valid                
        
    def parse_toml_manifest(self, manifest_filepath):
        """
        Parses the manifest file

        :param str manifest_filepath: the path to the toml manifest file
        :return: the dictionaries of the tf configuration files
        """
        plan = defaultdict()
        docker_settings = defaultdict()
        # Read toml manifest file and populate terraform configuration templates
        try:
            with open(manifest_filepath, "rt") as fin:
                parsed_toml = toml.load(fin)
                try:
                    plan["builder"] = parsed_toml["plan"]["builder"]
                    plan["app_directory"] = parsed_toml["plan"]["app_directory"]
                    if not os.path.isdir(plan["app_directory"]):
                        logging.error("The provided app_directory does not exist")
                        sys.exit("-1")
                    plan["output_directory"] = parsed_toml["plan"]["output_directory"]
                    plan["name"] = parsed_toml["plan"]["name"]
                    plan["version"] = parsed_toml["plan"]["version"]
                    plan["executable"] = parsed_toml["plan"]["executable"]
                    plan["command"] = parsed_toml["plan"]["command"]
                    docker_settings["hub_username"] = parsed_toml["docker"]["hub_username"]
                    docker_settings["hub_password"] = parsed_toml["docker"]["hub_password"]

                    servers_conf = parsed_toml["aws"]["servers"]
                    if not self.validate_ec2_servers_number(servers_conf["instances_per_az"]):
                        parsed_toml = {}
                    elif not self.validate_az_number(servers_conf["availability_zones"], servers_conf["regions"]):
                        parsed_toml = {}

                except KeyError as e:
                    logging.error("Error: The .toml manifest file does not have the required format")
                    logging.error(e)
                    parsed_toml = {}
        except OSError as e:
            logging.error(e)

        return parsed_toml, plan, docker_settings




