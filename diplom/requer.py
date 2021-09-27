import requests
import json
from decouple import config
#from webpars import Parser


url = "https://hotels4.p.rapidapi.com/locations/search"

class Requer:
    def __init__(self, sity) -> None:
        self.set = False
        self.sity = sity
        self.sityfile = sity + '.json'
        self.querystring = {"query":sity, "locale":"ru"}
        self.headers = {
            'x-rapidapi-host': config('HOST'),
            'x-rapidapi-key': config('KEY')
            }
        response = requests.request("GET", url, headers=self.headers, params=self.querystring)
        self.dataset(self.sityfile, json.loads(response.text))

    def dataset(self, file, gets):
        mark = [d for d in gets["suggestions"] if d['group'] in ["HOTEL_GROUP", "LANDMARK_GROUP"]]
        if mark[0]['entities']:
            with open(file, 'w')as op:
                json.dump(mark, op, indent=4)
            self.set = True


#Requer('sochi')