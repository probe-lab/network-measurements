import os
import json
import shutil
import logging
from collections import defaultdict
# custom modules
from . import s3_api


class TerraformApi(object):

    def __init__(self):
        self.es_region = "us-east-1"
        self.obs_module_name = "observatory"
        self.es_module_name = "elasticsearch"

    def compile_main_tf(self, servers_conf):
        """
        Creates the main Terraform configuration file
        
        :param servers_conf: the configuration parameters for the requested servers
        :type: defaultdict
        :return: True/False depending on whether the creation of the main.tf.json file was successful
        :rtype: bool
        """
        success = False
        main_tf_json = {
            "module": defaultdict(dict)
        }
        try:
            for region in servers_conf["regions"]:
                module_name = "observatory-{}".format(region)
                main_tf_json["module"][module_name]["region"] = region
                main_tf_json["module"][module_name]["source"] = "./{}".format(self.obs_module_name)
                main_tf_json["module"][module_name]["instance_type"] = servers_conf["instance_type"]

            if len(main_tf_json["module"]) > 0:
                es_module_name = "es-domain-{}".format(self.es_region)
                main_tf_json["module"][module_name]["region"] = self.es_region
                main_tf_json["module"][module_name]["source"] = "./{}".format(self.es_module_name)

                with open("main.tf.json", "wt") as fout:
                    json.dump(main_tf_json, fout, indent=4)
                success = True
            else:
                logging.error("No valid region name was provided in the .toml manifest file.")

        except KeyError as e:
            logging.error("The .toml manifest file does not have the required format...")
            logging.error(e)
        except OSError as e:
            logging.error("Failed to create the main.tf.json Terraform file...")
            logging.error(e)
        return success         
        
    def compile_obs_variables_tf(self, parsed_toml):
        """
        Creates the variables Terraform configuration file for the observatory module

        :param parsed_toml: the configuration parameters in the .toml manifest file
        :type servers_conf: defaultdict
        :return:False if creation of the configuration file fails, otherwise the values of the variables
        :rtype: bool/defaultdict
        """
        success = False
        variables_tf_json = {
            "variable": {
                "access_key": {"default": ""},
                "secret_key": {"default": ""},
                "instances_per_az": {"default": 1},
                "availability_zones": {"default": 1},
                "instance_type": {"default": {}},
                "ssh_pub_key": {"default": {}},
                "ssh_private_key": {"default": {}},
                "s3_bucket_name": {"default": {}},
                "region": {},
                "es_domain": {},
                "es_username": {},
                "es_password": {}
            }
        }
        
        try:
            metrics_s3_bucket = parsed_toml["aws"]["metrics_s3_bucket"]
            es_username = parsed_toml["elasticsearch"]["username"]
            es_password = parsed_toml["elasticsearch"]["password"]
            es_domain = parsed_toml["elasticsearch"]["domain"]

            servers_conf = parsed_toml["aws"]["servers"]
            instance_type = servers_conf["instance_type"]
            ssh_pub_key = servers_conf["ssh_pub_key"]
            ssh_private_key = servers_conf["ssh_private_key"]
            instances_per_az = servers_conf["instances_per_az"]
            availability_zones = servers_conf["availability_zones"]
        except KeyError as e:
            logging.error("The .toml manifest file does not have the required format...")
            logging.error(e)
        
        try:
            variables_tf_json["variable"]["instance_type"]["default"] = instance_type
            variables_tf_json["variable"]["ssh_pub_key"]["default"] = ssh_pub_key
            variables_tf_json["variable"]["ssh_private_key"]["default"] = ssh_private_key
            variables_tf_json["variable"]["s3_bucket_name"]["default"] = metrics_s3_bucket
            variables_tf_json["variable"]["es_username"]["default"] = es_username
            variables_tf_json["variable"]["es_password"]["default"] = es_password
            variables_tf_json["variable"]["es_domain"]["default"] = es_domain
            variables_tf_json["variable"]["instances_per_az"]["default"] = instances_per_az
            variables_tf_json["variable"]["availability_zones"]["default"] = availability_zones

            current_credentials = s3_api.get_credentials()
            variables_tf_json["variable"]["access_key"]["default"] = current_credentials.access_key
            variables_tf_json["variable"]["secret_key"]["default"] = current_credentials.secret_key

            var_tf_file = "./{}/variables.tf.json".format(self.obs_module_name)

            with open(var_tf_file, "wt") as fout:
                json.dump(variables_tf_json, fout, indent=4)

            # copy the variables file in the app directory
            var_app_file = os.path.join(parsed_toml["plan"]["app_directory"], os.path.basename(var_tf_file))

            shutil.copy(var_tf_file, var_app_file)
            shutil.copy(var_tf_file, "./{}/variables.tf.json".format(self.es_module_name))
            success = variables_tf_json
        except KeyError as e:
            logging.error("The .toml manifest file does not have the required format...")
            logging.error(e)
        except OSError as e:
            logging.error("Failed to create the variables.tf.json Terraform file...")
            logging.error(e)
        return success