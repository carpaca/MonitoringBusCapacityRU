import sqlite3
import requests
import json
import time
from datetime import datetime

conn = sqlite3.connect('test.db')
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
        #print(resp_vehicles)
        ID_idx = 1

        for ct in range(0, len(resp_vehicles['data']['1323'])):
            # print(ct, ':', resp_vehicles['data']['1323'][ct]['arrival_estimates'][0]['route_id'])
            # route_name_fetch = c.execute("""SELECT routeNAME FROM TEST_ROUTES WHERE routeID = routeID""")
            curr_routeID = resp_vehicles['data']['1323'][ct]['route_id']
            ag_route_name_fetch = c.execute("SELECT routeNAME FROM TEST_ROUTES WHERE routeID = ?",
                                            (curr_routeID,)).fetchone()
            ag_route_str = ag_route_name_fetch[0]
            # print(ag_route_name)

            stop_list = []
            arrive_list = []
            stop_name = []
            lat_long = []

            for idx1 in range(len(resp_vehicles['data']['1323'][ct]['arrival_estimates'])):
                stop_list.append(resp_vehicles['data']['1323'][ct]['arrival_estimates'][idx1]['stop_id'])
                arrive_list.append(resp_vehicles['data']['1323'][ct]['arrival_estimates'][idx1]['arrival_at'])
                stop_string = ' '.join(stop_list)
                arrive_string = ' '.join(arrive_list)

                # if len(resp_vehicles['data']['1323'][ct]['arrival_estimates'][idx1]) > 0:
                curr_stop_id = resp_vehicles['data']['1323'][ct]['arrival_estimates'][idx1]['stop_id']
                curr_stop_name_tup = c.execute("SELECT stopNAME FROM STOPS WHERE stopID = ?",
                                               (curr_stop_id,)).fetchone()
                curr_stop_name = curr_stop_name_tup[0]
                stop_name.append(curr_stop_name)
                stop_name_str = ', '.join(stop_name)
                # print(stop_list)
                # else:
                # stop_name_str = 'n/a'

                lat = resp_vehicles['data']['1323'][ct]['location']['lat']
                long = resp_vehicles['data']['1323'][ct]['location']['lng']
                # print(type(lat))

                lat = str(lat)
                long = str(long)
                lat_long = lat + ',' + long
                # print(lat_long)

            if len(resp_vehicles['data']['1323'][ct]['arrival_estimates']) >= 1:
                c.execute(
                    "INSERT OR REPLACE INTO TEST_TABLE VALUES (:ID, :vehicleID, :capacity, :routeNAME, :routeID, :stopName, :nextSTOP, :arrivals, :lat_long)",
                    {'ID': ID_idx,
                     'vehicleID': resp_vehicles['data']['1323'][ct]['call_name'],
                     'capacity': capacity,
                     'routeNAME': ag_route_str,
                     'routeID': resp_vehicles['data']['1323'][ct]['route_id'],
                     'stopName': stop_name_str,
                     'nextSTOP': stop_string,
                     'arrivals': arrive_string,
                     'lat_long': lat_long})
            else:
                c.execute(
                    "INSERT OR REPLACE INTO TEST_TABLE VALUES (:ID, :vehicleID, :capacity, :routeNAME, :routeID, :stopName, :nextSTOP, :arrivals, :lat_long)",
                    {'ID': ID_idx,
                     'vehicleID': resp_vehicles['data']['1323'][ct]['call_name'],
                     'capacity': capacity,
                     'routeNAME': ag_route_str,
                     'routeID': resp_vehicles['data']['1323'][ct]['route_id'],
                     'stopName': 'n/a',
                     'nextSTOP': 'n/a',
                     'arrivals': 'n/a',
                     'lat_long': 'n/a'})

            ID_idx = ID_idx + 1
            conn.commit()

    def input_agency(self):
        resp_agency = self.agency()

        ID_idx1 = 1

        # input data from get_agency to ROUTE table
        for ct1 in range(len(resp_agency['data']['1323'])):
            stop_st = ' '.join(resp_agency['data']['1323'][ct1]['stops'])
            c.execute("INSERT OR REPLACE INTO TEST_ROUTES VALUES (:ID, :routeID, :routeNAME, :STOPS)",
                      {'ID': ID_idx1,
                       'routeID': resp_agency['data']['1323'][ct1]['route_id'],
                       'routeNAME': resp_agency['data']['1323'][ct1]['long_name'],
                       'STOPS': stop_st})
            ID_idx1 = ID_idx1 + 1
            conn.commit()

    def input_busses(self):
        resp_vehicles = self.vehicles()

        ID_idx2 = 1
        # stop_list = []
        # resp_vehicles['data']['1323'][ct2]['arrival_estimates'][0]['stop_id']
        for ct2 in range(len(resp_vehicles['data']['1323'])):
            stop_list = []
            arrive_list = []
            for idx in range(len(resp_vehicles['data']['1323'][ct2]['arrival_estimates'])):
                stop_list.append(resp_vehicles['data']['1323'][ct2]['arrival_estimates'][idx]['stop_id'])
                arrive_list.append(resp_vehicles['data']['1323'][ct2]['arrival_estimates'][idx]['arrival_at'])
                stop_string = ' '.join(stop_list)
                arrive_string = ' '.join(arrive_list)
                # print(stop_list)
            if len(resp_vehicles['data']['1323'][ct2]['arrival_estimates']) >= 1:
                c.execute(
                    "INSERT OR REPLACE INTO BUSSES VALUES (:ID, :vehicle_number, :capacity, :route, :stop, :arrivals, :lat, :long)",
                    {'ID': ID_idx2,
                     'vehicle_number': resp_vehicles['data']['1323'][ct2]['vehicle_id'],
                     'capacity': 0,
                     'route': resp_vehicles['data']['1323'][ct2]['route_id'],
                     'stop': stop_string,
                     'arrivals': arrive_string,
                     'lat': resp_vehicles['data']['1323'][ct2]['location']['lat'],
                     'long': resp_vehicles['data']['1323'][ct2]['location']['lng']})
            else:
                c.execute(
                    "INSERT OR REPLACE INTO BUSSES VALUES (:ID, :vehicle_number, :capacity, :route, :stop, :arrivals, :lat, :long)",
                    {'ID': ID_idx2,
                     'vehicle_number': resp_vehicles['data']['1323'][ct2]['vehicle_id'],
                     'capacity': 0,
                     'route': resp_vehicles['data']['1323'][ct2]['route_id'],
                     'stop': 'none',
                     'arrivals': ' ',
                     'lat': resp_vehicles['data']['1323'][ct2]['location']['lat'],
                     'long': resp_vehicles['data']['1323'][ct2]['location']['lng']})

            ID_idx2 = ID_idx2 + 1
            conn.commit()

    def input_stops(self):
        resp_stops = self.stops()
        #print(resp_stops)
        ID_idx3 = 1

        # input data from get_stops to STOPS table
        for ct3 in range(len(resp_stops['data'])):
            # print(len(resp_stops['data']))
            route_st = ' '.join(resp_stops['data'][ct3]['routes'])
            c.execute("INSERT OR REPLACE INTO STOPS VALUES (:ID, :stopID, :stopNAME, :routes)",
                      {'ID': ID_idx3,
                       'stopID': resp_stops['data'][ct3]['stop_id'],
                       'stopNAME': resp_stops['data'][ct3]['name'],
                       'routes': route_st})
            ID_idx3 = ID_idx3 + 1
            conn.commit()

    def run(self, capacity):
        #conn = sqlite3.connect('test.db')
        #c = conn.cursor()
        #wait_time = 10
        #itt = 1
        #print('capacity = ', capacity)
        c.execute("DELETE FROM TEST_ROUTES;")
        #print("here")
        self.input_agency()

        c.execute("DELETE FROM STOPS;")
        self.input_stops()

    #while True:
        c.execute("DELETE FROM TEST_TABLE;",)
        c.execute("DELETE FROM BUSSES;",)
        conn.commit

        #print(capacity)

        self.input_vehicles(capacity)
        self.input_busses()

        #print("table updates: ", itt, "| date/time: ", datetime.now())
        #itt = itt + 1
        #time.sleep(wait_time)

#if __name__ == '__main__':
#    transloc = transloc()
#    transloc.run(counter)
