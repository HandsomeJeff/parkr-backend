
import requests
import SimpleHTTPServer
import SocketServer
import json
import ast
from datetime import datetime

from itertools import izip_longest

with open('fixed.json') as f:
    data = json.load(f)

def merge(a, b):
    res = {}
    keys = set(a.keys()) | set(b.keys())
    if isinstance(a.values()[0], list):
        res = {k: list(izip_longest(a.get(k, [None]), b.get(k, [None]))) for k in keys}
    else:
        res = {k: [a.get(k, None), b.get(k, None)] for k in keys}
    return res

class fiveLots(object):

    def __init__(self, *args, **kwargs):
        super(fiveLots, self).__init__(*args, **kwargs)

    def availableLots(self, cp_no):

        with open('cp_lots.json') as r:
            cp_now = json.load(r)

        for x in cp_now:
            if x['carpark_number'] == cp_no:
                for y in x['carpark_info']:
                    return {'lots_type' : y['lot_type'],
                            'total_lots_available' : int(y['total_lots']),
                            'lots_available' : int(y['lots_available'])
                            }
        return {}


    def nearestLots(self, lat, lon, limit=0.3):
        global data
        cplist = {}
        threshold = limit * limit
        for x in data:
            xdiff = abs(float(data[x]['lat'])-lat)
            ydiff = abs(float(data[x]['lon'])-lon)
            diff_sq = xdiff * xdiff + ydiff * ydiff
            if diff_sq < threshold:
                cplist[data[x]['car_park_no']] = {'diff_sq' : diff_sq,
                                                  'key_num' : x
                                                  }
        
        if len(cplist) > 5:
            temp = {}
            templist = []
            for x in cplist.values():
                templist.append(x['diff_sq'])
            templist.sort()
            for y in templist[:5]:
                for x in cplist:
                    if cplist[x]['diff_sq'] == y:
                        temp[x] = cplist[x]
            cplist = temp

        carparks = {}

        for key in cplist.keys():
            key = str(key)
            x = cplist[key]['key_num']
            carparks[key] = {'carpark no.' : key,
                             'address' : str(data[x]['address']),
                             'lat' : float(data[x]['lat']),
                             'lon' : float(data[x]['lon']),
                             'car_park_type' : str(data[x]['car_park_type']),
                             'type_of_parking' : str(data[x]['type_of_parking_system']),
                             'short_term_parking' : str(data[x]['short_term_parking']),
                             'free_parking' : str(data[x]['free_parking']),
                             'night_parking' : str(data[x]['night_parking'])
                             }
            avail = self.availableLots(key)
            for lot in avail:
                carparks[key][lot] = avail[lot]
                          
        final = {'result' : [x for x in carparks.values()]}
        return final

##    for x in carparks:
##        print x + ' : ' + str(carparks[x]) + '\n'
##        print len(carparks[x].values())

##
##1)Carpark No. (String)
##2)address (string)
##3)lat (float)(WGS84 format)
##4)Lon (float)
##5)car_park_type (string)
##6)type_of_parking (string)
##7) short_term_parking (string)
##8) free_parking (string)
##9) night_parking (string)
##10) total_lots_available (string)
##11) lots_available (string)
##12) lots_type (string)

##xinp = int(raw_input("Enter X-coordinate: "))
##yinp = int(raw_input("Enter Y-coordinate: "))
##tinp = int(raw_input("Enter tolerance: "))
##cplist = nearestLots(xinp, yinp, tinp)
##
##print '\n----------------------------------'
##print '|     Nearby carpark numbers     |'
##print '----------------------------------\n'
##print cplist

##print "Input lat = 1.3, lon = 103.5\n"
##print nearestLots(lat=1.3,lon=103.5)

