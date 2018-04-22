#!/usr/bin/python
# coding: utf-8
# ==============================================================================
# Script Name     : lld-vgc.py
# Tool Version    : 1.0.0
# Arguments       : -
# Options         : -h, --help       show this help message and exit
#                 : -v, --version    show version and exit
#                 : -p, --partition  show all partition
# Usage           : $0 [Option]
# OS Version      : CentOS release 5, 6, 7
# ==============================================================================
# Date          Author        Changes
# 2018/04/10    Yuta Akama    New Creation
# ==============================================================================
# --+----1----+----2----+----3----+----4----+----5----+----6----+----7----+----8

import json
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
                       '-v', '--version',
                       action='version',
                       version='1.0.0',
                       help='show version and exit'
                   )
parser.add_argument(
                       '-p', '--partition',
                       action='store_true',
                       help='show all partition'
                   )
args = parser.parse_args()

if __name__ == "__main__":
    p1 = subprocess.Popen(['vgc-monitor', '-f', 'json'], stdout=subprocess.PIPE)
    stdout, stderr = p1.communicate()
    data = list()
    json_data = json.loads(stdout.decode('utf-8'))
    for vgc in json_data:
        if isinstance(json_data[vgc], list):
            cardnumber = -1
            for card in json_data[vgc]:
                cardnumber += 1
                cardname = card['cardName']
                if (args.partition == True or args.partition == True):
                  if isinstance(card['partitionDetails'], list):
                    partnumber = -1
                    for part in card['partitionDetails']:
                        partnumber += 1
                        partname = part['partName']
                        data.append({
                            "{#VGCCARDNUMBER}": cardnumber,
                            "{#VGCCARDNAME}": cardname,
                            "{#VGCPARTNUMBER}": partnumber,
                            "{#VGCPARTNAME}": partname
                        })
                else:
                        data.append({
                            "{#VGCCARDNUMBER}": cardnumber,
                            "{#VGCCARDNAME}": cardname
                        })
    print(json.dumps({"data": data}, indent=4))
