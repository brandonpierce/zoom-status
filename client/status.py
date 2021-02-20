#!/usr/bin/env python3

import argparse
import json
import psutil
import requests

in_a_meeting = 0

parser = argparse.ArgumentParser()

parser.add_argument('-s', default='localhost')
parser.add_argument('-p', default=5000)

args = parser.parse_args()

if args.s:
    server = args.s

if args.p:
    port = args.p

url = 'http://' + server + ':' + str(port) + '/zoom'


for proc in psutil.process_iter(['pid', 'name']):
    name = proc.info['name']

    if name.startswith('CptHost'):
        in_a_meeting = 1


headers = {'Content-Type': 'application/json'}

if in_a_meeting == 1:
    print('in a meeting')
    data = {'status': 'online'}
    r = requests.put(url, data=json.dumps(data), headers=headers)
    print(r)
else:
    print('not in a meeting')
    data = {'status': 'offline'}
    r = requests.put(url, data=json.dumps(data), headers=headers)
    print(r)
