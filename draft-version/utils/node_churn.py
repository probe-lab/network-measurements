#!/usr/bin/env python3
import os
import json
import time
import pyasn
import logging
import requests
import ipaddress
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor


class Parser(object):

    class IPAddr(object):

        def __init__(self, asn, city=False, country=False):
            self.asn = asn
            self.city = city
            self.country = country
            self.nodes = set()
            self.instances = set()
            self.datetimes = set()


    def __init__(self):
        self.dates = defaultdict(list)
        self.ips = defaultdict(self.IPAddr)
        self.autsys = defaultdict(set)
        self.peers = defaultdict(lambda: defaultdict(set))
        self.port_count = defaultdict(set)
        self.asndb = pyasn.pyasn("ipasn.20201029.dat")

    def parse_files(self):
        """

        :return:
        """
        subdirs = [x[0][2:] for x in os.walk('.')]
        for subdir in subdirs:
            if subdir.startswith("i-0"):
                filenames = [os.path.join(subdir, f) for f in os.listdir(subdir) if f.endswith(".json")]
                with ThreadPoolExecutor(max_workers=20) as executor:
                    executor.map(self.parse_peer_graph, filenames)
                print("Finished parsing {}".format(subdir))

    def parse_peer_graph(self, crawl_file):
        """
        Parses the output of the DHT scrapper to collect the peers

        :param str crawl_file: the output of the DHT scrapper service
        """
        filename = os.path.basename(crawl_file)
        subdir = crawl_file.replace(filename, "")[:-2]
        with open(crawl_file, "rt") as fin:
            try:
                filename_fields = filename.split("_")
                start_datetime = filename_fields[1]
                start_datetime_obj = datetime.strptime(start_datetime, '%d-%m-%y--%H:%M:%S')
                ts = int(start_datetime_obj.timestamp())
                self.dates[subdir].append(ts)
                crawl_data = json.load(fin)
                if "Nodes" in crawl_data:
                    for node in crawl_data["Nodes"]:
                        peer_id = node["NodeID"]
                        for address in node["MultiAddrs"]:
                            address_fields = address.split("/")
                            if address_fields[1] == "ip4":
                                ipaddr = ipaddress.ip_address(address_fields[2])
                                if len(address_fields) == 5:
                                    port = address_fields[4]
                                    if ipaddr.is_global:
                                        ipaddr = str(ipaddr)
                                        self.peers[peer_id]["ipaddrs"].add(ipaddr)
                                        self.peers[peer_id]["ports"].add(port)
                                        self.peers[peer_id]["datetimes"].add(ts)
                                        asn, prefix = self.asndb.lookup(ipaddr)
                                        self.autsys[asn].add(ipaddr)
                                        if ipaddr not in self.ips:
                                            self.ips[ipaddr] = self.IPAddr(asn)
                                        self.ips[ipaddr].nodes.add(peer_id)
                                        self.ips[ipaddr].datetimes.add(ts)
            except json.decoder.JSONDecodeError:
                logging.error("Failed to parse file {}".format(crawl_file))

    def write_output(self):
        """
        Outputs the results in a text file

        :return: None
        """
        with open("ipfs-ipaddrs-nodes.txt", "wt") as fout:
            for ipaddr in self.ips:
                nodes = self.ips[ipaddr].nodes
                fout.write("{}\t{}\t{}\n".format(ipaddr, len(nodes), ','.join(nodes)))

        with open("ipfs-nodes.txt", "wt") as fout:
            for node_id in self.peers:
                ipaddresses = self.peers[node_id]["ipaddrs"]
                ports = self.peers[node_id]["ports"]
                datetimes = [str(t) for t in self.peers[node_id]["datetimes"]]
                fout.write("{}\t{}\t{}\t".format(node_id, len(ipaddresses), ','.join(ipaddresses)))
                fout.write("{}\t{}\t".format(len(ports), ','.join(ports)))
                fout.write("{}\t{}\t".format(len(datetimes), ','.join(datetimes)))

    def visualize_churn(self):
        """
        Generates plots

        :return:
        """
        node_counts = defaultdict(int)
        for ipaddr in self.ips:
            count = len(self.ips[ipaddr].nodes)
            if count > 1:
                node_counts[count] += 1
        nodes_x = np.arange(len(node_counts))
        nodes_y = list()
        for nodes, count in node_counts.items():
            nodes_y.append(count)
        print(node_counts)
        plt.bar(nodes_y, nodes_y)
        plt.xlabel("Number of IPFS Peer IDs")
        plt.ylabel("Number of IP Addresses")
        plt.savefig("ip_to_nodes.png")

parser = Parser()
parser.parse_files()
parser.write_output()
parser.visualize_churn()

