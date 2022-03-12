import json
import requests

#This file is where it uses the USGS earthquake API to harvests the data.
url = "https://earthquake.usgs.gov/fdsnws/event/1/query?"

#Latitude and longtitude of the Philippines from January 1 2022 to present
dict_parameter = {"format": "geojson", "starttime": "2022-01-01",
              "minlatitude":5, "minlongitude":115, "maxlatitude":21,"maxlongitude":130}

e_data = requests.get(url, params=dict_parameter)
data = e_data.json()

with open('earthquake.json', 'w') as f:
    json.dump(data, f, indent=2)
