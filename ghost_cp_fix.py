
import requests
import json
import ast
import time



with open('cp_lots.json') as r:
    cp_now = json.load(r)

with open('cp_info.json') as f:
    data = json.load(f)

print 'Number of api carparks: ',len(cp_now)
print 'Number of csv carparks: ',len(data)

new = open('fixed.json', 'w')
new.write('{')

i=0

for x in data:
    for y in cp_now:
        if data[x]['car_park_no'] == y['carpark_number']:
            new.write('"'+str(i)+'":')
            json.dump(data[x], new)
            new.write(',\n')
            i+=1

new.write('}')
new.close()
print 'Number of common carparks: ',i
