import sqlite3
import requests
import json
import time
from datetime import datetime

conn = sqlite3.connect('capstone.db')
c = conn.cursor()

"""transloc object that puts information into database.
    Work with EvoPeopleCounter object in multithread to get sensor data"""

class transloc:

    #conn = sqlite3.connect('test.db')
    #c = conn.cursor()

    def __init__(self):
        self.url_vehicles = "https://transloc-api-1-2.p.rapidapi.com/vehicles.json"
        self.url_agency = "https://transloc-api-1-2.p.rapidapi.com/routes.json"
        self.url_stops = "https://transloc-api-1-2.p.rapidapi.com/stops.json"
        self.querystring = {"agencies": "1323", "callback": "call"}
        self.headers = {
        'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
        'x-rapidapi-key': 'API KEY'
        }
        #self.conn = sqlite3.connect('test.db')
        #self.c = self.conn.cursor()

    def vehicles(self):
        response = requests.request("GET", self.url_vehicles, headers=self.headers, params=self.querystring)
        response_json = json.loads(response.text.encode('utf8'))

        return response_json

    def agency(self):
        response = requests.request("GET", self.url_agency, headers=self.headers, params=self.querystring)
        response_json = json.loads(response.text.encode('utf8'))

        return response_json

    def stops(self):
        response = requests.request("GET", self.url_stops, headers=self.headers, params=self.querystring)
        response_json = json.loads(response.text.encode('utf8'))

        return response_json

    def input_vehicles(self, capacity):
        resp_vehicles = self.vehicles()
        ID_idx = 1

        for ct in range(0, len(resp_vehicles['data']['1323'])):
            c.execute(
                "INSERT OR REPLACE INTO VEHICLES VALUES (:ID, :vehicleID, :capacity, :routeID)",
                {'ID': ID_idx,
                 'vehicleID': resp_vehicles['data']['1323'][ct]['call_name'],
                 'capacity': capacity,
                 'routeID': resp_vehicles['data']['1323'][ct]['route_id']
                 })

            ID_idx = ID_idx + 1
            conn.commit()

    def input_agency(self):
        resp_agency = self.agency()

        ID_idx1 = 1

        # input data from get_agency to ROUTE table
        for ct1 in range(len(resp_agency['data']['1323'])):
            stop_st = ' '.join(resp_agency['data']['1323'][ct1]['stops'])
            c.execute("INSERT OR REPLACE INTO ROUTES VALUES (:ID, :routeID, :routeNAME)",
                      {'ID': ID_idx1,
                       'routeID': resp_agency['data']['1323'][ct1]['route_id'],
                       'routeNAME': resp_agency['data']['1323'][ct1]['long_name'],
                       })
            ID_idx1 = ID_idx1 + 1
            conn.commit()

    def input_stops(self):
        resp_stops = self.stops()
        #print(resp_stops)
        ID_idx3 = 1

        # input data from get_stops to STOPS table
        for ct3 in range(len(resp_stops['data'])):
            # print(len(resp_stops['data']))
            #route_st = ' '.join(resp_stops['data'][ct3]['routes'])
            c.execute("INSERT OR REPLACE INTO STOPS VALUES (:ID, :stopID, :stopNAME)",
                      {'ID': ID_idx3,
                       'stopID': resp_stops['data'][ct3]['stop_id'],
                       'stopNAME': resp_stops['data'][ct3]['name'],
                       })
            ID_idx3 = ID_idx3 + 1
            conn.commit()

    def run(self, capacity):
        #conn = sqlite3.connect('test.db')
        #c = conn.cursor()
        #wait_time = 10
        #itt = 1
        #print('capacity = ', capacity)
        c.execute("DELETE FROM ROUTES;")
        #print("here")
        self.input_agency()

        c.execute("DELETE FROM STOPS;")
        self.input_stops()

    #while True:
        c.execute("DELETE FROM VEHICLES;",)
        #c.execute("DELETE FROM BUSSES;",)
        conn.commit

        #print(capacity)

        self.input_vehicles(capacity)
        #self.input_busses()

        #print("table updates: ", itt, "| date/time: ", datetime.now())
        #itt = itt + 1
        #time.sleep(wait_time)

#if __name__ == '__main__':
#    transloc = transloc()
#    transloc.run(counter)
