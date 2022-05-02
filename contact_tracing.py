import sqlite3
import time
from datetime import datetime as dt
from twilio.rest import Client

con = sqlite3.connect('capstone.db', check_same_thread=False)
cur = con.cursor()

def contact_tracing(netid):
	#add items to see if students are on bus at the same time
	contact_list = {}
	student_list = []
	bus, date, on, off = get_buslist(netid)
	for i in range(len(bus)):
		print("\ntracing bus",bus[i],"\n", flush=True)
		for student in get_passengers(bus[i]):
			b, d, n, f = get_buslist(student)
			for j in range(len(b)):
				if bus[i] == b[j]:
					if check_overlap(time.strptime(date[i],"%Y-%m-%d"), time.strptime(on[i],"%H:%M:%S"), time.strptime(off[i],"%H:%M:%S"), time.strptime(d[j],"%Y-%m-%d"), time.strptime(n[j],"%H:%M:%S"), time.strptime(f[j],"%H:%M:%S")):
						if student[0] != netid:
							contact_list[student] = [bus[i], date[i]]
							student_list.append(student[0])
							result = cur.execute('SELECT COVID FROM USERS WHERE netID = ?', (netid,)).fetchone()[0]
							if result == 1:
								notify(student[0])
							else:
								continue
						else:
							continue
	return contact_list, student_list

def notify(netid):
	#twlio goes here
	print(netid)
	account_sid = 'AC19fc5049169130ebe290e252b3dc8617'
	auth_token = '723edabc5cc3933294d263436bc99a05'
	client = Client(account_sid, auth_token)

	result = cur.execute('SELECT COVID, phone_num FROM USERS WHERE netID = ?', (netid,)).fetchone()
	covid = result[0]
	phone = result[1]

	#send message
	message = client.messages.create(
		messaging_service_sid='MGf67d763cc479f499f28fd8f1745cc857',
		body='You have been in contact with someone who has tested positive for COVID-19',
		to=phone
	)

	print(message.sid)
	print('message sent to', netid)

	return

def get_buslist(netid):
	print("\ntracing student",netid,"\n", flush=True)
	student = get_student(netid)
	bus = student[6].split(',')
	date = student[8].split(',')
	on = student[9].split(',')
	off = student[10].split(',')
	return bus, date, on, off

def get_student(netid):
	return cur.execute("select * from USERS where netID = '%s'" %(netid)).fetchone()

def get_passengers(id):
	print(cur.execute("select netID from USERS where vehicle like '%s'" %('%'+id+'%')).fetchall())
	return cur.execute("select netID from USERS where vehicle like '%s'" %('%'+id+'%')).fetchall()

def got_on_bus(vehicle_id, netid):
	bus, date, on, off = get_buslist(netid)
	time = dt.now()
	bus = bus.append(vehicle_id)
	date = date.append('%d-%d-%d' %(time.year,time.day,time.month))
	on = on.append('%d:%d:%d' %(time.hour,time.minute,time.second))
	off = off.append('%d:%d:%d' %(time.hour,time.minute,time.second))
	b = ",".join(bus)
	d = ",".join(date)
	o1 = ",".join(on)
	o2 = ",".join(off)
	cur.execute("update USERS set vehicle = '%s'" (b))
	cur.execute("update USERS set vehicle = '%s'" (d))
	cur.execute("update USERS set time_on = '%s'" (o1))
	cur.execute("update USERS set time_off = '%s'" (o2))

def undo_get_on_bus(vehicle_id, netid):
	time = dt.now()
	dat
	bus, date, on, off = get_buslist(netid)
	if bus[-1] == vehicle_id:
		del bus[-1]
		del date[-1]
		del on[-1]
		del off[-1]
		b = ",".join(bus)
		d = ",".join(date)
		o1 = ",".join(on)
		o2 = ",".join(off)
		cur.execute("update USERS set vehicle = '%s'" (b))
		cur.execute("update USERS set vehicle = '%s'" (d))
		cur.execute("update USERS set time_on = '%s'" (o1))
		cur.execute("update USERS set time_off = '%s'" (o2))

def got_off_bus(vehicle_id, netid):
	#map get off bus time
	bus, date, on, off = get_buslist(netid)
	if bus[-1] == vehicle_id:
		off[-1] = '%d:%d:%d' %(time.hour,time.minute,time.second)
		o = ",".join(off)
		cur.execute("update USERS set time_off = '%s'" (o2))

def check_overlap(d1, n1, x1, d2, n2, x2):
	return (d1==d2 and (((n1 <= x2) and (x1 >= x2)) or ((n2 <= x1) and (x2 >= x1))))

def student_info(netid):
	student = get_student(netid)
	if student == None:
		return ("No Student Found", "XXX-XXX-XXXX", "XXXX", {}, {})
	phone = student[3]
	grad = student[5]
	b, d, o, _ = get_buslist(netid)
	busses = {b[i]:[d[i],o[i]] for i in range(len(b))}
	contacts = contact_tracing(netid)
	return (netid, phone, grad, busses, contacts)