import json
from datetime import datetime

#This part is for decoding the earthquake.json file where all the harvested data were stored.

with open('earthquake.json') as f:
    data = json.load(f)

#Code for converting the the timestamp into readable date and time.
def timestamp(timestamp):
    timestamp = str(timestamp)
    timestamp = timestamp[:10] + '.' + timestamp[10:]
    timestamp_float = float(timestamp)
    timestamp_convert = datetime.fromtimestamp(timestamp_float).strftime('%B %d,%Y %I:%M:%S %p')
    timestamp = timestamp_convert
    return timestamp

"""Code for printing the data. Also it shows that how I use the timestamp function to convert
    the timestamp into a readable date and time. [example: timestamp(1647008065753) ]
"""
for i in data['features']:
    data_place = i['properties']['place']
    data_mag = i['properties']['mag']
    data_time = i['properties']['time']
    data_time_updated = i['properties']['updated']
    data_tsunami = i['properties']['tsunami']
    if data_time == data_time and data_time_updated == data_time_updated:
        data_time = timestamp(data_time)
        data_time_updated = timestamp(data_time_updated)
    print(f'Origin date and time: {data_time}')
    print(f'Updated date and time: {data_time_updated}')
    print(f'Place: {data_place}')
    print(f'Magnitude: {data_mag}')
    print(f'Number of tsunami: {data_tsunami}\n')
#time
#We indicate the date and time when the earthquake initiates rupture, which is known as the "origin" time.
# Note that large earthquakes can continue rupturing for many 10's of seconds or every 100 milliseoncds.
#updated time
#Time when the event was most recently updated. Times are reported in milliseconds




# data_time = str(data_time)
#         data_time = data_time[:10] + '.' + data_time[10:]
#         data_time2 = float(data_time)
#         date_time3 = datetime.fromtimestamp(data_time2).strftime('%B %d,%Y %I:%M:%S %p')
#         data_time = date_time3

