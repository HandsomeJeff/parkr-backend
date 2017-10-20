
import requests
import json
import ast
import time


api_key = #INSERT API KEY HERE

headers = {'api-key' : api_key}

url = 'https://api.data.gov.sg/v1/transport/carpark-availability'




while True:
    r = requests.get(url, headers=headers)

    cp_now = r.json()['items'][0]['carpark_data']

    with open('cp_lots.json', 'w') as f:
        json.dump(cp_now,f)

    print 'done'
    time.sleep(60)
