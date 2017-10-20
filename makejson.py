
import json
import csv


cfile = open('cp_long_lat.csv', 'r')
jfile = open('cp_info.json', 'w')

fieldnames = ("car_park_no","address","x_coord","y_coord","car_park_type","type_of_parking_system","short_term_parking","free_parking","night_parking","lat","lon","lat_rad","lon_rad")

reader = csv.DictReader(cfile, fieldnames)

jfile.write('{')

i = 0

for row in reader:
    jfile.write('"' + str(i) +'":')
    json.dump(row, jfile)
    jfile.write(',\n')
    i+=1

jfile.write('}')
