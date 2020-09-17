#!/usr/bin/env python3

import os
import json


public_ips = set()
keypath = False

# Parse the terraform state to extract the instance details
with open("terraform.tfstate") as fin:
    tf_state = json.load(fin)
    for resource in tf_state["resources"]:
        if resource["type"] == "aws_instance":
            for instance in resource["instances"]:
                public_ip = instance["attributes"]["public_ip"]
                public_ips.add(public_ip)
        elif resource["type"] == "aws_key_pair":
            for instance in resource["instances"]:
                keypath = instance["attributes"]["tags"]["Name"]

if keypath and len(public_ips) > 0:
    # Create the ansible working directory
    if not os.path.exists('ansible'):
        os.makedirs('ansible')

    # Create the ansible hosts file
    with open("ansible/hosts", "wt") as fout:
        fout.write("[probes]\n")
        for ip in public_ips:
            fout.write("{} ansible_user=ubuntu ansible_ssh_private_key_file={}".format(ip, keypath))
