
import requests
import json
import ast
import time


headers = {'api-key' : 'mpFZtGkgI5aN4vVc671QE1o12hmRjvaS'}

url = 'https://api.data.gov.sg/v1/transport/carpark-availability'




while True:
    r = requests.get(url, headers=headers)

    cp_now = r.json()['items'][0]['carpark_data']

    with open('cp_lots.json', 'w') as f:
        json.dump(cp_now,f)

    print 'done'
    time.sleep(60)
