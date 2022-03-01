import time
from datetime import datetime
#from multiprocessing import Process, Queue
from transloc import transloc
#from EvoPeopleCounter import EvoPeopleCounter

"""separate scripts to continually update tables.
    still working on running this and the sensor code at the same time."""

#sensor = EvoPeopleCounter()
trans = transloc()

#def input_data():
itt = 1
wait_time = 5
capacity_prev = None

while True:
    capacity = capacity_prev
    trans.run(capacity)

    #if capacity == None:
    #    continue

    print('capacity = ', capacity)

    print("table updates: ", itt, "| date/time: ", datetime.now())
    itt = itt + 1
    time.sleep(wait_time)
