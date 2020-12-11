#!/usr/bin/env python3
import os
import json
import time
import boto3
import logging
import requests
import ipaddress
from collections import defaultdict


class Parser(object):

    def __init__(self, username, passwd, domain):
        self.fout = open("dht_peer.txt", "at")
        self.peers = defaultdict(lambda: defaultdict())
        self.incomplete_line = False
        self.username = username
        self.passwd = passwd
        self.domain = domain

    def ip2geo(self, ip):
        """
        Maps an IP address to a country and city

        :param ip: The IP address to geolocate
        :return:
        """
        r = requests.get("https://stat.ripe.net/data/maxmind-geo-lite/data.json?resource={}".format(ip))
        decoded_response = r.json()
        if "data" in decoded_response and "located_resources" in decoded_response["data"]:
            for resource in decoded_response["data"]["located_resources"]:
                prefix = resource["resource"]
                for location in resource["locations"]:
                    self.peers[ip]["city"] = location["city"]
                    self.peers[ip]["country"] = location["country"]
                    self.peers[ip]["latitude"] = location["latitude"]
                    self.peers[ip]["longitude"] = location["longitude"]

    def ip2asn(self, ip):
        """
        Maps an IP address to the ASN that owns it

        :param str ip: the IP address to map
        """
        r = requests.get("https://stat.ripe.net/data/prefix-overview/data.json?max_related=50&resource={}".format(ip))

        try:
            decoded_response = r.json()
            if "data" in decoded_response and "asns" in decoded_response["data"]:
                for asn in decoded_response["data"]["asns"]:
                    self.peers[ip]["asn"] = asn["asn"]
                    # self.peers[ip]["holder"] = asn["holder"]
        except json.decoder.JSONDecodeError:
            logging.error("Could not map the ASN for IP: {}".format(ip))
            self.retry_set[ip] += 1
            if self.retry_set[ip] == 10:
                del(self.retry_set[ip])

    def parse_peer_graph(self, crawl_file):
        """
        Parses the output of the DHT scrapper to collect the peers

        :param str crawl_file: the output of the DHT scrapper service
        """
        with open(crawl_file, "rt") as fin:
            print(crawl_file)
            crawl_data = json.load(fin)
            if "Nodes" in crawl_data:
                for node in crawl_data["Nodes"]:
                    peer_id = node["NodeID"]
                    for address in node["MultiAddrs"]:
                        address_fields = address.split("/")
                        if address_fields[1] == "ip4":
                            ipaddr = ipaddress.ip_address(address_fields[2])
                            if ipaddr.is_global and ipaddr not in self.peers:
                                self.ip2asn(ipaddr)
                                self.ip2geo(ipaddr)
                                self.peers[ipaddr]["time"] = int(time.time())
                                self.peers[ipaddr]["peer_id"] = peer_id
                                if "asn" not in self.peers[ipaddr]:
                                    self.peers[ipaddr]["asn"] = "None"
                                try:
                                    d = {
                                        "ip": str(ipaddr),
                                        "asn": self.peers[ipaddr]["asn"],
                                        "city": self.peers[ipaddr]["city"],
                                        "country": self.peers[ipaddr]["country"],
                                        "latitutde": self.peers[ipaddr]["latitude"],
                                        "longitude": self.peers[ipaddr]["longitude"]
                                    }

                                    cmd = "curl -XPOST -u {}:{} https://{}/crawls/_doc/ -d '{}' -H 'Content-Type: application/json'".format(self.username,
                                                                                                self.passwd,
                                                                                                self.domain,
                                                                                                json.dumps(d))
                                    os.system(cmd)
                                except KeyError as e:
                                    print(e)


with open("variables.tf.json", "rt") as fin:
    output_dir = "output_data_crawls"
    vars = json.load(fin)
    domain = vars["variable"]["es_domain"]["default"]
    passwd = vars["variable"]["es_password"]["default"]
    username = vars["variable"]["es_username"]["default"]
    access_key = vars["variable"]["access_key"]["default"]
    secret_key = vars["variable"]["secret_key"]["default"]
    #session = boto3.session.Session(
    #    region_name='us-west-2', aws_access_key_id=access_key,
    #aws_secret_access_key=secret_key)
    client = boto3.client('es', region_name='us-east-1', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    response = client.describe_elasticsearch_domain(
        DomainName=domain
    )
    domain_endpoint = response["DomainStatus"]["Endpoint"]
    parser = Parser(username, passwd, domain_endpoint)
    for peers_file in os.listdir(output_dir):
        peers_filepath = os.path.join(output_dir, peers_file)
        print(peers_filepath)
        parser.parse_peer_graph(peers_filepath)
