import time
from datetime import datetime
from multiprocessing import Process, Queue
from transloc import transloc
from EvoPeopleCounter import EvoPeopleCounter

#run sensor and get latest reading

def read_sensor():
    capacity = None
    while True:
        header, sensor_id, data = sensor.get_ranges()
        if header == b'PC':
            capacity = data[0]
            sensor_queue.put(capacity)
            #capacity_prev = capacity
            print(capacity)
        else:
            #sensor_queue.put(capacity)
            continue

def input_data():
    itt = 1
    wait_time = 2
    capacity_prev = None
    cap_prev = None
    cap_list = []
    t_current = datetime.now()
    while True:
        if not sensor_queue.empty():
            capacity = sensor_queue.get(block=True)
            #trans.run(capacity)
            capacity_prev = capacity
            cap_list.append(capacity)

        else:
            capacity = capacity_prev
            #trans.run(capacity)

        t_new = datetime.now()

        t_diff = (t_new - t_current)
        #print(type(t_diff))
        t_diff = t_diff.total_seconds()
        #print(t_diff)

        if t_diff >= 5:
            print("time has passed: ", t_diff, cap_list)
            t_current = datetime.now()
            if len(cap_list) == 0:
                trans.run(cap_prev)
                print('capacity = ', cap_prev)

                print("table updates: ", itt, "| date/time: ", datetime.now())
                itt = itt + 1
            else:
                cap_curr = cap_list[len(cap_list)-1]
                trans.run(cap_curr)
                print('capacity = ', cap_curr)

                print("table updates: ", itt, "| date/time: ", datetime.now())
                itt = itt + 1
                cap_prev = cap_curr
                cap_list = []


if __name__ == '__main__':
    sensor = EvoPeopleCounter()
    trans = transloc()
    sensor_queue = Queue()

    read_process = Process(target=read_sensor)

    read_process.start()

    try:
        input_data()
    finally:
        read_process.join()
