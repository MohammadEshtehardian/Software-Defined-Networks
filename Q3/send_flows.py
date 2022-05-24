from urllib import response
import requests
from requests.auth import HTTPBasicAuth
import json
import os


# Iterate files in flows folder
for filename in os.listdir('flows'):
    data = {} # dict for saving json file
    with open(f'flows/{filename}') as json_file:
        data = json.load(json_file) # data from json file
    node = int(filename.split('_')[0])
    # url that we want for sending request
    url = f'http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:{node}/flow-node-inventory:table/0/flow/{data["flow"][0]["id"]}' 
    response = requests.put(url, json=data, auth=HTTPBasicAuth('admin', 'admin')) # sending put request for adding flows
    