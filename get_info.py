from transloc import transloc
from datetime import datetime
from dateutil import parser
import pytz
from math import trunc

trans = transloc()
"""
Functions to get information needed for the app: transloc API, db ride history, contact tracing information
"""
#transloc API function calls
def route_vehicles(routeID, stopID):
    vehicle = trans.vehicles()
    time_now = datetime.now(pytz.utc)
    stops = []
    arrivals = []
    vehicles = []
    #x = vehicle

    for i in range(len(vehicle['data']['1323'])):
        route_id = vehicle['data']['1323'][i]['route_id']
        if route_id == routeID:
            for j in range(len(vehicle['data']['1323'][i]['arrival_estimates'])):
                stop_id = vehicle['data']['1323'][i]['arrival_estimates'][j]['stop_id']
                if stop_id == stopID:
                    arr_time = parser.parse(vehicle['data']['1323'][i]['arrival_estimates'][j]['arrival_at'])
                    stops.append(vehicle['data']['1323'][i]['arrival_estimates'][j]['stop_id'])
                    arrivals.append(arr_time)
                    vehicles.append(vehicle['data']['1323'][i]['call_name'])

    info = []
    for i in range(len(arrivals)):
        info.append(arrivals[i])
        info.append(vehicles[i])

    key_list = ["arrivals", "vehicle"]
    bus_info = []

    for k in range(0, len(info), 2):
        bus_info.append({key_list[0]: info[k], key_list[1]: info[k+1]})

    for l in range(len(bus_info)):
        bus_info[l]['arrivals'] = trunc((bus_info[l]['arrivals'] - time_now).total_seconds() / 60)

    bus_info = sorted(bus_info, key=lambda x: x['arrivals'])

    if len(arrivals) >= 3:
        arrivals1 = bus_info[0]['arrivals']
        arrivals2 = bus_info[1]['arrivals']
        arrivals3 = bus_info[2]['arrivals']

        vehicles1 = bus_info[0]['vehicle']
        vehicles2 = bus_info[1]['vehicle']
        vehicles3 = bus_info[2]['vehicle']

        return arrivals1, arrivals2, arrivals3, vehicles1, vehicles2, vehicles3

    elif len(arrivals) == 2:
        arrivals1 = bus_info[0]['arrivals']
        arrivals2 = bus_info[1]['arrivals']
        arrivals3 = None

        vehicles1 = bus_info[0]['vehicle']
        vehicles2 = bus_info[1]['vehicle']
        vehicles3 = None

        return arrivals1, arrivals2, arrivals3, vehicles1, vehicles2, vehicles3


    elif len(arrivals) == 1:
        arrivals1 = bus_info[0]['arrivals']
        arrivals2 = None
        arrivals3 = None

        vehicles1 = bus_info[0]['vehicle']
        vehicles2 = None
        vehicles3 = None

        return arrivals1, arrivals2, arrivals3, vehicles1, vehicles2, vehicles3

    else:
        arrivals1 = None
        arrivals2 = None
        arrivals3 = None

        vehicles1 = None
        vehicles2 = None
        vehicles3 = None

        return arrivals1, arrivals2, arrivals3, vehicles1, vehicles2, vehicles3

#get student ride history
def student_rec(vehicle, time_on, date): #get information for student records page
    vehicle = vehicle.split(",")
    time = time_on.split(",")
    date = date.split(",")

    full_list = []
    for i in range(len(vehicle)):
        full_list.append(vehicle[i])
        full_list.append(date[i])
        full_list.append(time[i])

    key_list = ["vehicle", "date", "time"]
    n = len(full_list)
    ride_info = []

    for l in range(0, n, 3):
        ride_info.append({key_list[0]: full_list[l], key_list[1]: full_list[l + 1], key_list[2]: full_list[l + 2]})

    return ride_info

#get contact tracing information
def contact_rec(contact_dict, student_list):
    key_list = ["student", "vehicle_num", "date"]
    contact_data = []
    for i in range(len(contact_dict)):
        current_student = (student_list[i],)
        ride_list = contact_dict.get(current_student)
        contact_data.append(student_list[i])
        contact_data.append(ride_list[0])
        contact_data.append(ride_list[1])

    n = len(contact_data)
    contact_info = []

    for l in range(0, n, 3):
        contact_info.append({key_list[0]: contact_data[l], key_list[1]: contact_data[l + 1], key_list[2]: contact_data[l + 2]})

    return contact_info

"""if __name__ == '__main__':
    print('hello')"""
