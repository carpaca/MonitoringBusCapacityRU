import datetime
import sqlite3
from flask import Flask, redirect, url_for, render_template, request, session
from flask_bcrypt import Bcrypt
from get_info import *
from contact_tracing import *
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
bcrypt = Bcrypt()

conn = sqlite3.connect('capstone.db', check_same_thread=False)
c = conn.cursor()

#remove comment code for capacity in each bus webpage

@app.route("/")
def home():
	if 'user_id' not in session:
		return redirect(url_for('login'))
	elif session['user_stat'] == 'student':
		return render_template("homepage.html")
	elif session['user_stat'] == 'administrator':
		return redirect((url_for('studentRecord')))

@app.route("/Weekend-1-bus", methods=['POST', 'GET'])
def weekendOneBus():

	if 'user_id' not in session:
		return redirect(url_for('login'))

	else:
		if 'current_bus' in session:
			session.pop('current_bus', None)
			session.pop('current_time', None)
			session.pop('current_route', None)

		capacity = c.execute("SELECT capacity FROM VEHICLES WHERE ID = 1").fetchone()
		capacity = capacity[0]

		#capacity = 0

		arrivals_CAstudentctr1, arrivals_CAstudentctr2, arrivals_CAstudentctr3, vehicles_CAstudentctr1, vehicles_CAstudentctr2, vehicles_CAstudentctr3 = route_vehicles('4012650', '4259014')
		arrivals_SACN1, arrivals_SACN2, arrivals_SACN3, vehicles_SACN1, vehicles_SACN2, vehicles_SACN3  = route_vehicles('4012650', '4229496')
		arrivals_yard1, arrivals_yard2, arrivals_yard3, vehicles_yard1, vehicles_yard2, vehicles_yard3 = route_vehicles('4012650', '4259014')
		arrivals_HCNB1, arrivals_HCNB2, arrivals_HCNB3, vehicles_HCNB1, vehicles_HCNB2, vehicles_HCNB3 = route_vehicles('4012650', '4229620')
		arrivals_science1, arrivals_science2, arrivals_science3, vehicles_science1, vehicles_science2, vehicles_science3 = route_vehicles('4012650', '4259018')
		arrivals_BSC1, arrivals_BSC2, arrivals_BSC3, vehicles_BSC1, vehicles_BSC2, vehicles_BSC3 = route_vehicles('4012650', '4259062')
		arrivals_livi1, arrivals_livi2, arrivals_livi3, vehicles_livi1, vehicles_livi2, vehicles_livi3 = route_vehicles('4012650', '4229570')
		arrivals_SACS1, arrivals_SACS2, arrivals_SACS3, vehicles_SACS1, vehicles_SACS2, vehicles_SACS3 = route_vehicles('4012650', '4229696')
		arrivals_redOak1, arrivals_redOak2, arrivals_redOak3, vehicles_redOak1, vehicles_redOak2, vehicles_redOak3 = route_vehicles('4012650', '4259030')
		arrivals_lipman1, arrivals_lipman2, arrivals_lipman3, vehicles_lipman1, vehicles_lipman2, vehicles_lipman3 = route_vehicles('4012650', '4229596')
		arrivals_biel1, arrivals_biel2, arrivals_biel3, vehicles_biel1, vehicles_biel2, vehicles_biel3 = route_vehicles('4012650', '4259054')
		arrivals_henderson1, arrivals_henderson2, arrivals_henderson3, vehicles_henderson1, vehicles_henderson2, vehicles_henderson3 = route_vehicles('4012650', '4259722')
		arrivals_gibbons1, arrivals_gibbons2, arrivals_gibbons3, vehicles_gibbons1, vehicles_gibbons2, vehicles_gibbons3 = route_vehicles('4012650', '4259058')
		arrivals_CollegeHall1, arrivals_CollegeHall2, arrivals_CollegeHall3, vehicles_CollegeHall1, vehicles_CollegeHall2, vehicles_CollegeHall3 = route_vehicles('4012650', '4253700')
		arrivals_SoCam1, arrivals_SoCam2, arrivals_SoCam3, vehicles_SoCam1, vehicles_SoCam2, vehicles_SoCam3 = route_vehicles('4012650', '4253718')

		if request.method == 'POST':
			if request.form.get('YES') == 'enter_CASC1' and arrivals_CAstudentctr1 != None and arrivals_CAstudentctr1 <= 3:
				vehicle_number = vehicles_CAstudentctr1
			elif request.form.get('YES') == 'enter_CASC2' and arrivals_CAstudentctr2 != None and arrivals_CAstudentctr2 <= 3:
				vehicle_number = vehicles_CAstudentctr2
			elif request.form.get('YES') == 'enter_CASC3' and arrivals_CAstudentctr3 != None and arrivals_CAstudentctr3 <= 3:
				vehicle_number = vehicles_CAstudentctr3
			elif request.form.get('YES') == 'enter_SACN1' and arrivals_SACN1 != None and arrivals_SACN1 <= 3:
				vehicle_number = vehicles_SACN1
			elif request.form.get('YES') == 'enter_SACN2' and arrivals_SACN2 != None and arrivals_SACN2 <= 3:
				vehicle_number = vehicles_SACN2
			elif request.form.get('YES') == 'enter_SACN3' and arrivals_SACN3 != None and arrivals_SACN3 <= 3:
				vehicle_number = vehicles_SACN3
			elif request.form.get('YES') == 'enter_yard1' and arrivals_yard1 != None and arrivals_yard1 <= 3:
				vehicle_number = vehicles_yard1
			elif request.form.get('YES') == 'enter_yard2' and arrivals_yard2 != None and arrivals_yard2 <= 3:
				vehicle_number = vehicles_yard2
			elif request.form.get('YES') == 'enter_yard3' and arrivals_yard3 != None and arrivals_yard3 <= 3:
				vehicle_number = vehicles_yard3
			elif request.form.get('YES') == 'enter_HCNB1' and arrivals_HCNB1 != None and arrivals_HCNB1 <= 3:
				vehicle_number = vehicles_HCNB1
			elif request.form.get('YES') == 'enter_HCNB2' and arrivals_HCNB2 != None and arrivals_HCNB2 <= 3:
				vehicle_number = vehicles_HCNB2
			elif request.form.get('YES') == 'enter_sciences1' and arrivals_science1 != None and arrivals_science1 <= 3:
				vehicle_number = vehicles_science1
			elif request.form.get('YES') == 'enter_sciences2' and arrivals_science2 != None and arrivals_science2 <= 3:
				vehicle_number = vehicles_science2
			elif request.form.get('YES') == 'enter_sciences3' and arrivals_science3 != None and arrivals_science3 <= 3:
				vehicle_number = vehicles_science3
			elif request.form.get('YES') == 'enter_BSC1' and arrivals_BSC1 != None and arrivals_BSC1 <= 3:
				vehicle_number = vehicles_BSC1
			elif request.form.get('YES') == 'enter_BSC2' and arrivals_BSC2 != None and arrivals_BSC2 <= 3:
				vehicle_number = vehicles_BSC2
			elif request.form.get('YES') == 'enter_BSC3' and arrivals_BSC3 != None and arrivals_BSC3 <= 3:
				vehicle_number = vehicles_BSC3
			elif request.form.get('YES') == 'enter_livi1' and arrivals_livi1 != None and arrivals_livi1 <= 3:
				vehicle_number = vehicles_livi1
			elif request.form.get('YES') == 'enter_livi2' and arrivals_livi2 != None and arrivals_livi2 <= 3:
				vehicle_number = vehicles_livi2
			elif request.form.get('YES') == 'enter_livi3' and arrivals_livi3 != None and arrivals_livi3 <= 3:
				vehicle_number = vehicles_livi3
			elif request.form.get('YES') == 'enter_SACS1' and arrivals_SACS1 != None and arrivals_SACS1 <= 3:
				vehicle_number = vehicles_SACS1
			elif request.form.get('YES') == 'enter_SACS2' and arrivals_SACS2 != None and arrivals_SACS2 <= 3:
				vehicle_number = vehicles_SACS2
			elif request.form.get('YES') == 'enter_SACS3' and arrivals_SACS3 != None and arrivals_SACS3 <= 3:
				vehicle_number = vehicles_SACS3
			elif request.form.get('YES') == 'enter_redoak1' and arrivals_redOak1 != None and arrivals_redOak1 <= 3:
				vehicle_number = vehicles_redOak1
			elif request.form.get('YES') == 'enter_redoak2' and arrivals_redOak2 != None and arrivals_redOak2 <= 3:
				vehicle_number = vehicles_redOak2
			elif request.form.get('YES') == 'enter_redoak3' and arrivals_redOak3 != None and arrivals_redOak3 <= 3:
				vehicle_number =vehicles_redOak3
			elif request.form.get('YES') == 'enter_lipman1' and arrivals_lipman1 != None and arrivals_lipman1 <= 3:
				vehicle_number = vehicles_lipman1
			elif request.form.get('YES') == 'enter_lipman2' and arrivals_lipman2 != None and arrivals_lipman2 <= 3:
				vehicle_number = vehicles_lipman2
			elif request.form.get('YES') == 'enter_lipman3' and arrivals_lipman3 != None and arrivals_lipman3 <= 3:
				vehicle_number = vehicles_lipman3
			elif request.form.get('YES') == 'enter_biel1' and arrivals_biel1 != None and arrivals_biel1 <= 3:
				vehicle_number = vehicles_biel1
			elif request.form.get('YES') == 'enter_biel2' and arrivals_biel2 != None and arrivals_biel2 <= 3:
				vehicle_number = vehicles_biel2
			elif request.form.get('YES') == 'enter_biel3' and arrivals_biel3 != None and arrivals_biel3 <= 3:
				vehicle_number = vehicles_biel3
			elif request.form.get('YES') == 'enter_henderson1' and arrivals_henderson1 != None and arrivals_henderson1 <= 3:
				vehicle_number = vehicles_henderson1
			elif request.form.get('YES') == 'enter_henderson2' and arrivals_henderson2 != None and arrivals_henderson2 <= 3:
				vehicle_number = vehicles_henderson2
			elif request.form.get('YES') == 'enter_henderson3' and arrivals_henderson3 != None and arrivals_henderson3 <= 3:
				vehicle_number = vehicles_henderson3
			elif request.form.get('YES') == 'enter_gibbons1' and arrivals_gibbons1 != None and arrivals_gibbons1 <= 3:
				vehicle_number = vehicles_gibbons1
			elif request.form.get('YES') == 'enter_gibbons2' and arrivals_gibbons2 != None and arrivals_gibbons2 <= 3:
				vehicle_number = vehicles_gibbons2
			elif request.form.get('YES') == 'enter_gibbons3' and arrivals_gibbons3 != None and arrivals_gibbons3 <= 3:
				vehicle_number = vehicles_gibbons3
			elif request.form.get('YES') == 'enter_collegehall1' and arrivals_CollegeHall1 != None and arrivals_CollegeHall1 <= 3:
				vehicle_number = vehicles_CollegeHall1
			elif request.form.get('YES') == 'enter_collegehall2' and arrivals_CollegeHall2 != None and arrivals_CollegeHall2 <= 3:
				vehicle_number = vehicles_CollegeHall2
			elif request.form.get('YES') == 'enter_collegehall3' and arrivals_CollegeHall3 != None and arrivals_CollegeHall3 <= 3:
				vehicle_number = vehicles_CollegeHall3
			elif request.form.get('YES') == 'enter_SoCam1' and arrivals_SoCam1 != None and arrivals_SoCam1 <= 3:
				vehicle_number = vehicles_SoCam1
			elif request.form.get('YES') == 'enter_SoCam2' and arrivals_SoCam2 != None and arrivals_SoCam2 <= 3:
				vehicle_number = vehicles_SoCam2
			elif request.form.get('YES') == 'enter_SoCam3' and arrivals_SoCam3 != None and arrivals_SoCam3 <= 3:
				vehicle_number = vehicles_SoCam3
			else:
				return redirect(url_for('weekendOneBus'))

			session['current_bus'] = vehicle_number
			session['current_time'] = datetime.now().strftime("%H:%M:%S")
			session['current_route'] = 'Route Weekend-1'

			return redirect(url_for('exit_bus'))

	return render_template('WeekendOneBus.html',
							arrivals_CAstudentctr1=arrivals_CAstudentctr1,
							arrivals_CAstudentctr2=arrivals_CAstudentctr2,
							arrivals_CAstudentctr3=arrivals_CAstudentctr3,

							arrivals_SACN1=arrivals_SACN1,
							arrivals_SACN2=arrivals_SACN2,
							arrivals_SACN3=arrivals_SACN3,

							arrivals_yard1=arrivals_yard1,
							arrivals_yard2=arrivals_yard2,
							arrivals_yard3=arrivals_yard3,

							arrivals_HCNB1=arrivals_HCNB1,
							arrivals_HCNB2=arrivals_HCNB2,
							arrivals_HCNB3=arrivals_HCNB3,

							arrivals_science1=arrivals_science1,
							arrivals_science2=arrivals_science2,
							arrivals_science3=arrivals_science3,

							arrivals_BSC1=arrivals_BSC1,
							arrivals_BSC2=arrivals_BSC2,
							arrivals_BSC3=arrivals_BSC3,

							arrivals_livi1=arrivals_livi1,
							arrivals_livi2=arrivals_livi2,
							arrivals_livi3=arrivals_livi3,

							arrivals_SACS1=arrivals_SACS1,
							arrivals_SACS2=arrivals_SACS2,
							arrivals_SACS3=arrivals_SACS3,

							arrivals_redOak1=arrivals_redOak1,
							arrivals_redOak2=arrivals_redOak2,
							arrivals_redOak3=arrivals_redOak3,


							arrivals_lipman1=arrivals_lipman1,
							arrivals_lipman2=arrivals_lipman2,
							arrivals_lipman3=arrivals_lipman3,


							arrivals_biel1=arrivals_biel1,
							arrivals_biel2=arrivals_biel2,
							arrivals_biel3=arrivals_biel3,


							arrivals_henderson1=arrivals_henderson1,
							arrivals_henderson2=arrivals_henderson2,
							arrivals_henderson3=arrivals_henderson3,


							arrivals_gibbons1=arrivals_gibbons1,
							arrivals_gibbons2=arrivals_gibbons2,
							arrivals_gibbons3=arrivals_gibbons3,


							arrivals_CollegeHall1=arrivals_CollegeHall1,
							arrivals_CollegeHall2=arrivals_CollegeHall2,
							arrivals_CollegeHall3=arrivals_CollegeHall3,


							arrivals_SoCam1=arrivals_SoCam1,
							arrivals_SoCam2=arrivals_SoCam2,
							arrivals_SoCam3=arrivals_SoCam3,

							capacity=capacity

							)

@app.route("/A-bus", methods=['GET', 'POST'])
def ABus():
	if 'user_id' not in session:
		return redirect(url_for('login'))

	else:
		if 'current_bus' in session:
			session.pop('current_bus', None)
			session.pop('current_time', None)
			session.pop('current_route', None)

		capacity = c.execute("SELECT capacity FROM VEHICLES WHERE ID = 1").fetchone()
		capacity = capacity[0]

		#capacity = 0

		arrivals_CASC1, arrivals_CASC2, arrivals_CASC3, vehicles_CASC1, vehicles_CASC2, vehicles_CASC3 = route_vehicles('4015032', '4259014')
		arrivals_yard1, arrivals_yard2, arrivals_yard3, vehicles_yard1, vehicles_yard2, vehicles_yard3 = route_vehicles('4015032', '4229620')
		arrivals_SACN1, arrivals_SACN2, arrivals_SACN3, vehicles_SACN1, vehicles_SACN2, vehicles_SACN3 = route_vehicles('4015032', '4229496')
		arrivals_stadium1, arrivals_stadium2, arrivals_stadium3 , vehicles_stadium1, vehicles_stadium2, vehicles_stadium3 = route_vehicles('4015032', '4259010')
		arrivals_hill1, arrivals_hill2, arrivals_hill3, vehicles_hill1, vehicles_hill2, vehicles_hill3 = route_vehicles('4015032', '4259016')
		arrivals_sciences1, arrivals_sciences2, arrivals_sciences3, vehicles_sciences1, vehicles_sciences2, vehicles_sciences3 = route_vehicles('4015032', '4259018')
		arrivals_BSC1, arrivals_BSC2, arrivals_BSC3, vehicles_BSC1, vehicles_BSC2, vehicles_BSC3 = route_vehicles('4015032', '4259062')
		arrivals_werblin1, arrivals_werblin2, arrivals_werblin3, vehicles_weblin1, vehicles_werblin2, vehicles_werblin3 = route_vehicles('4015032', '4259568')

		if request.method == 'POST':
			if request.form.get('YES') == 'enter_CASC1' and arrivals_CASC1 != None and arrivals_CASC1 <= 3:
				vehicle_number = vehicles_CASC1
			elif request.form.get('YES') == 'enter_CASC2' and arrivals_CASC2 != None and arrivals_CASC2 <= 3:
				vehicle_number = vehicles_CASC2
			elif request.form.get('YES') == 'enter_CASC3' and arrivals_CASC3 != None and arrivals_CASC3 <= 3:
				vehicle_number = vehicles_CASC3
			elif request.form.get('YES') == 'enter_yard1' and arrivals_yard1 != None and arrivals_yard1 <= 3:
				vehicle_number = vehicles_yard1
			elif request.form.get('YES') == 'enter_yard2' and arrivals_yard2 != None and arrivals_yard2 <= 3:
				vehicle_number = vehicles_yard2
			elif request.form.get('YES') == 'enter_yard3' and arrivals_yard3 != None and arrivals_yard3 <= 3:
				vehicle_number = vehicles_yard3
			elif request.form.get('YES') == 'enter_SACN1' and arrivals_SACN1 != None and arrivals_SACN1 <= 3:
				vehicle_number = vehicles_SACN1
			elif request.form.get('YES') == 'enter_SACN2' and arrivals_SACN2 != None and arrivals_SACN2 <= 3:
				vehicle_number = vehicles_SACN2
			elif request.form.get('YES') == 'enter_SACN3' and arrivals_SACN3 != None and arrivals_SACN3 <= 3:
				vehicle_number = vehicles_SACN3
			elif request.form.get('YES') == 'enter_CASC1' and arrivals_CASC1 != None and arrivals_CASC1 <= 3:
				vehicle_number = vehicles_CASC1
			elif request.form.get('YES') == 'enter_CASC2' and arrivals_CASC2 != None and arrivals_CASC2 <= 3:
				vehicle_number = vehicles_CASC2
			elif request.form.get('YES') == 'enter_CASC3' and arrivals_CASC3 != None and arrivals_CASC3 <= 3:
				vehicle_number = vehicles_CASC3
			elif request.form.get('YES') == 'enter_hill1' and arrivals_hill1 != None and arrivals_hill1 <= 3:
				vehicle_number = vehicles_hill1
			elif request.form.get('YES') == 'enter_hill2' and arrivals_hill2 != None and arrivals_hill2 <= 3:
				vehicle_number = vehicles_hill2
			elif request.form.get('YES') == 'enter_hill3' and arrivals_hill3 != None and arrivals_hill3 <= 3:
				vehicle_number = vehicles_hill3
			elif request.form.get('YES') == 'enter_sciences1' and arrivals_sciences1 != None and arrivals_sciences1 <= 3:
				vehicle_number = vehicles_sciences1
			elif request.form.get('YES') == 'enter_sciences2' and arrivals_sciences2 != None and arrivals_sciences2 <= 3:
				vehicle_number = vehicles_sciences2
			elif request.form.get('YES') == 'enter_sciences3' and arrivals_sciences3 != None and arrivals_sciences3 <= 3:
				vehicle_number = vehicles_sciences3
			elif request.form.get('YES') == 'enter_BSC1' and arrivals_BSC1 != None and arrivals_BSC1 <= 3:
				vehicle_number = vehicles_BSC1
			elif request.form.get('YES') == 'enter_BSC2' and arrivals_BSC2 != None and arrivals_BSC2 <= 3:
				vehicle_number = vehicles_BSC2
			elif request.form.get('YES') == 'enter_BSC3' and arrivals_BSC3 != None and arrivals_BSC3 <= 3:
				vehicle_number = vehicles_BSC3
			elif request.form.get('YES') == 'enter_werblin1' and arrivals_werblin1 != None and arrivals_werblin1 <= 3:
				vehicle_number = vehicles_weblin1
			elif request.form.get('YES') == 'enter_werblin2' and arrivals_werblin2 != None and arrivals_werblin2 <= 3:
				vehicle_number = vehicles_werblin2
			elif request.form.get('YES') == 'enter_werblin3' and arrivals_werblin3 != None and arrivals_werblin3 <= 3:
				vehicle_number = vehicles_werblin3
			else:
				return redirect(url_for('ABus'))

			session['current_bus'] = vehicle_number
			session['current_time'] = datetime.now().strftime("%H:%M:%S")
			session['current_route'] = 'Route A'

			return redirect(url_for('exit_bus'))

	return render_template("ABus.html",
						   arrivals_CASC1=arrivals_CASC1,
						   arrivals_CASC2=arrivals_CASC2,
						   arrivals_CASC3=arrivals_CASC3,

						   arrivals_yard1=arrivals_yard1,
						   arrivals_yard2=arrivals_yard2,
						   arrivals_yard3=arrivals_yard3,

						   arrivals_SACN1=arrivals_SACN1,
						   arrivals_SACN2=arrivals_SACN2,
						   arrivals_SACN3=arrivals_SACN3,

						   arrivals_stadium1=arrivals_stadium1,
						   arrivals_stadium2=arrivals_stadium2,
						   arrivals_stadium3=arrivals_stadium3,

						   arrivals_hill1=arrivals_hill1,
						   arrivals_hill2=arrivals_yard2,
						   arrivals_hill3=arrivals_hill3,

						   arrivals_sciences1=arrivals_sciences1,
						   arrivals_sciences2=arrivals_sciences2,
						   arrivals_sciences3=arrivals_sciences3,

						   arrivals_BSC1=arrivals_BSC1,
						   arrivals_BSC2=arrivals_BSC2,
						   arrivals_BSC3=arrivals_BSC3,

						   arrivals_werblin1=arrivals_werblin1,
						   arrivals_werblin2=arrivals_werblin2,
						   arrivals_werblin3=arrivals_werblin3,

						   capacity=capacity
						   )

@app.route("/B-bus", methods=['GET', 'POST'])
def BBus():

	if 'user_id' not in session:
		return redirect(url_for('login'))

	else:
		if 'current_bus' in session:
			session.pop('current_bus', None)
			session.pop('current_time', None)
			session.pop('current_route', None)

		capacity = c.execute("SELECT capacity FROM VEHICLES WHERE ID = 1").fetchone()
		capacity = capacity[0]

		#capacity = 0

		arrivals_LSC1, arrivals_LSC2, arrivals_LSC3, vehicles_LSC1, vehicles_LSC2, vehicles_LSC3 = route_vehicles('4015034', '4254110')
		arrivals_hill1, arrivals_hill2, arrivals_hill3, vehicles_hill1, vehicles_hill2, vehicles_hill3 = route_vehicles('4015034', '4259016')
		arrivals_sciences1, arrivals_sciences2, arrivals_sciences3, vehicles_sciences1, vehicles_sciences2, vehicles_sciences3 = route_vehicles('4015034', '4259018')
		arrivals_BSC1, arrivals_BSC2, arrivals_BSC3, vehicles_BSC1, vehicles_BSC2, vehicles_BSC3 = route_vehicles('4015034', '4259062')
		arrivals_livi1, arrivals_livi2, arrivals_livi3, vehicles_livi1, vehicles_livi2, vehicles_livi3 = route_vehicles('4015034', '4229570')

		if request.method == "POST":
			if request.form.get('YES') == 'enter_LSC1' and arrivals_LSC1 != None and arrivals_LSC1 <= 3:
				vehicle_number = vehicles_LSC1
			elif request.form.get('YES') == 'enter_LSC2' and arrivals_LSC2 != None and arrivals_LSC2 <= 3:
				vehicle_number = vehicles_LSC2
			elif request.form.get('YES') == 'enter_LSC3' and arrivals_LSC3 != None and arrivals_LSC3 <= 3:
				vehicle_number = vehicles_LSC3
			elif request.form.get('YES') == 'enter_hill1' and arrivals_hill1 != None and arrivals_hill1 <= 3:
				vehicle_number = vehicles_hill1
			elif request.form.get('YES') == 'enter_hill2' and arrivals_hill2 != None and arrivals_hill2 <= 3:
				vehicle_number = vehicles_hill2
			elif request.form.get('YES') == 'enter_hill3' and arrivals_hill3 != None and arrivals_hill3 <= 3:
				vehicle_number = vehicles_hill3
			elif request.form.get('YES') == 'enter_sciences1' and arrivals_sciences1 != None and arrivals_sciences1 <= 3:
				vehicle_number = vehicles_sciences1
			elif request.form.get('YES') == 'enter_sciences2' and arrivals_sciences2 != None and arrivals_sciences2 <= 3:
				vehicle_number = vehicles_sciences2
			elif request.form.get('YES') == 'enter_sciences3' and arrivals_sciences3 != None and arrivals_sciences3 <= 3:
				vehicle_number = vehicles_sciences3
			elif request.form.get('YES') == 'enter_BSC1' and arrivals_BSC1 != None and arrivals_BSC1 <= 3:
				vehicle_number = vehicles_BSC1
			elif request.form.get('YES') == 'enter_BSC2' and arrivals_BSC2 != None and arrivals_BSC2 <= 3:
				vehicle_number = vehicles_BSC2
			elif request.form.get('YES') == 'enter_BSC3' and arrivals_BSC3 != None and arrivals_BSC3 <= 3:
				vehicle_number = vehicles_BSC3
			elif request.form.get('YES') == 'enter_livi1' and arrivals_livi1 != None and arrivals_livi1 <= 3:
				vehicle_number = vehicles_livi1
			elif request.form.get('YES') == 'enter_livi2' and arrivals_livi2 != None and arrivals_livi2 <= 3:
				vehicle_number = vehicles_livi2
			elif request.form.get('YES') == 'enter_livi3' and arrivals_livi3 != None and arrivals_livi3 <= 3:
				vehicle_number = vehicles_livi3
			else:
				return redirect(url_for('BBus'))

			session['current_bus'] = vehicle_number
			session['current_time'] = datetime.now().strftime("%H:%M:%S")
			session['current_route'] = 'Route B'

			return redirect(url_for('exit_bus'))
	return render_template("BBus.html",
						   arrivals_LSC1=arrivals_LSC1,
						   arrivals_LSC2=arrivals_LSC2,
						   arrivals_LSC3=arrivals_LSC3,

						   arrivals_hill1=arrivals_hill1,
						   arrivals_hill2=arrivals_hill2,
						   arrivals_hill3=arrivals_hill3,

						   arrivals_sciences1=arrivals_sciences1,
						   arrivals_sciences2=arrivals_sciences2,
						   arrivals_sciences3=arrivals_sciences3,

						   arrivals_BSC1=arrivals_BSC1,
						   arrivals_BSC2=arrivals_BSC2,
						   arrivals_BSC3=arrivals_BSC3,

						   arrivals_livi1=arrivals_livi1,
						   arrivals_livi2=arrivals_livi2,
						   arrivals_livi3=arrivals_livi3,

						   capacity=capacity
						   )

@app.route("/C-bus", methods=['POST', 'GET'])
def CBus():
	if 'user_id' not in session:
		return redirect(url_for('login'))
	else:
		if 'current_bus' in session:
			session.pop('current_bus', None)
			session.pop('current_time', None)
			session.pop('current_route', None)

		capacity = c.execute("SELECT capacity FROM VEHICLES WHERE ID = 1").fetchone()
		capacity = capacity[0]

		#capacity = 0

		arrivals_stadium1, arrivals_stadium2, arrivals_stadium3, stadium_vehicles1, stadium_vehicles2, stadium_vehicles3 = route_vehicles('4014962', '4259010')
		arrivals_hillNB1, arrivals_hillNB2, arrivals_hillNB3, hillNB_vehicles1, hillNB_vehicles2, hillNB_vehicles3 = route_vehicles('4014962', '4259016')
		arrivals_allison1, arrivals_allison2, arrivals_allison3, arc_vehicles1, arc_vehicles2, arc_vehicles3 = route_vehicles('4014962', '4259048')
		arrivals_hillSB1, arrivals_hillSB2, arrivals_hillSB3, hillSB_vehicles1, hillSB_vehicles2, hillSB_vehicles3 = route_vehicles('4014962', '4231636')

		if request.method == 'POST':
			if request.form.get('YES') == 'enter_stadium1' and arrivals_stadium1 != None and arrivals_stadium1 <= 3:
				vehicle_number = stadium_vehicles1
			elif request.form.get('YES') == 'enter_stadium2' and arrivals_stadium2 != None and arrivals_stadium2 <= 3:
				vehicle_number = stadium_vehicles2
			elif request.form.get('YES') == 'enter_stadium3' and arrivals_stadium3 != None and arrivals_stadium3 <= 3:
				vehicle_number = stadium_vehicles3
			elif request.form.get('YES') == 'enter_hillNB1' and arrivals_hillNB1 != None and arrivals_hillNB1 <= 3:
				vehicle_number = hillNB_vehicles1
			elif request.form.get('YES') == 'enter_hillNB2' and arrivals_hillNB2 != None and arrivals_hillNB2 <= 3:
				vehicle_number = hillNB_vehicles2
			elif request.form.get('YES') == 'enter_hillNB3' and arrivals_hillNB3 != None and arrivals_hillNB3 <= 3:
				vehicle_number = hillNB_vehicles3
			elif request.form.get('YES') == 'enter_arc1' and arrivals_allison1 != None and arrivals_allison1 <= 3:
				vehicle_number = arc_vehicles1
			elif request.form.get('YES') == 'enter_arc2' and arrivals_allison2 != None and arrivals_allison2 <= 3:
				vehicle_number = arc_vehicles2
			elif request.form.get('YES') == 'enter_arc3' and arrivals_allison3 != None and arrivals_allison3 <= 3:
				vehicle_number = arc_vehicles3
			elif request.form.get('YES') == 'enter_hillSB1' and arrivals_hillSB1 != None and arrivals_hillSB1 <= 3:
				vehicle_number = hillSB_vehicles1
			elif request.form.get('YES') == 'enter_hillSB2' and arrivals_hillSB2 != None and arrivals_hillSB2 <= 3:
				vehicle_number = hillSB_vehicles2
			elif request.form.get('YES') == 'enter_hillSB3' and arrivals_hillSB3 != None and arrivals_hillSB3 <= 3:
				vehicle_number = hillSB_vehicles3
			else:
				return redirect(url_for('CBus'))

			session['current_bus'] = vehicle_number
			session['current_time'] = datetime.now().strftime("%H:%M:%S")
			session['current_route'] = 'Route C'

			return redirect(url_for('exit_bus'))

	return render_template("CBus.html",
						   arrivals_stadium1=arrivals_stadium1,
						   arrivals_stadium2=arrivals_stadium2,
						   arrivals_stadium3=arrivals_stadium3,

						   arrivals_hillNB1=arrivals_hillNB1,
						   arrivals_hillNB2=arrivals_hillNB2,
						   arrivals_hillNB3=arrivals_hillNB3,

						   arrivals_allison1=arrivals_allison1,
						   arrivals_allison2=arrivals_allison2,
						   arrivals_allison3=arrivals_allison3,

						   arrivals_hillSB1=arrivals_hillSB1,
						   arrivals_hillSB2=arrivals_hillSB2,
						   arrivals_hillSB3=arrivals_hillSB3,

						   capacity=capacity
						   )

@app.route("/EE-bus", methods=['POST', 'GET'])
def EEBus():
	if 'user_id' not in session:
		return redirect(url_for('login'))
	else:
		if 'current_bus' in session:
			session.pop('current_bus', None)
			session.pop('current_time', None)
			session.pop('current_route', None)

		capacity = c.execute("SELECT capacity FROM VEHICLES WHERE ID = 1").fetchone()
		capacity = capacity[0]

		#capacity = 0

		arrivals_CASC1, arrivals_CASC2, arrivals_CASC3, vehicles_CASC1, vehicles_CASC2, vehicles_CASC3 = route_vehicles('4015036', '4259014')
		arrivals_yard1, arrivals_yard2, arrivals_yard3, vehicles_yard1, vehicles_yard2, vehicles_yard3 = route_vehicles('4015036', '4229620')
		arrivals_SoCamSB1, arrivals_SoCamSB2, arrivals_SoCamSB3, vehicles_SoCamSB1, vehicles_SoCamSB2, vehicles_SoCamSB3 = route_vehicles('4015036', '4259050')
		arrivals_redoak1, arrivals_redoak2, arrivals_redoak3, vehicles_redoak1, vehicles_redoak2, vehicles_redoak3 = route_vehicles('4015036', '4259030')
		arrivals_lipman1, arrivals_lipman2, arrivals_lipman3, vehicles_lipman1, vehicles_lipman2, vehicles_lipman3 = route_vehicles('4015036', '4229596')
		arrivals_biel1, arrivals_biel2, arrivals_biel3, vehicles_biel1, vehicles_biel2, vehicles_biel3 = route_vehicles('4015036', '4259054')
		arrivals_henderson1, arrivals_henderson2, arrivals_henderson3, vehicles_henderson1, vehicles_henderson2, vehicles_henderson3 = route_vehicles('4015036', '4259722')
		arrivals_gibbons1, arrivals_gibbons2, arrivals_gibbons3, vehicles_gibbons1, vehicles_gibbons2, vehicles_gibbons3 = route_vehicles('4015036', '4259058')
		arrivals_collegehall1, arrivals_collegehall2, arrivals_collegehall3, vehicles_collegehall1, vehicles_collegehall2, vehicles_collegehall3 = route_vehicles('4015036', '4253700')
		arrivals_SoCamNB1, arrivals_SoCamNB2, arrivals_SoCamNB3, vehicles_SoCamNB1, vehicles_SoCamNB2, vehicles_SoCamNB3 = route_vehicles('4015036', '4253718')
		arrivals_SACN1, arrivals_SACN2, arrivals_SACN3, vehicles_SACN1, vehicles_SACN2, vehicles_SACN3 = route_vehicles('4015036', '4229496')


		if request.method == 'POST':
			if request.form.get('YES') == 'enter_CASC1' and arrivals_CASC1 != None and arrivals_CASC1 <= 3:
				vehicle_number = vehicles_CASC1
			elif request.form.get('YES') == 'enter_CASC2' and arrivals_CASC2 != None and arrivals_CASC2 <= 3:
				vehicle_number = vehicles_CASC2
			elif request.form.get('YES') == 'enter_CASC3' and arrivals_CASC3 != None and arrivals_CASC3 <= 3:
				vehicle_number = vehicles_CASC3
			elif request.form.get('YES') == 'enter_yard1' and arrivals_yard1 != None and arrivals_yard1 <= 3:
				vehicle_number = vehicles_yard1
			elif request.form.get('YES') == 'enter_yard2' and arrivals_yard2 != None and arrivals_yard2 <= 3:
				vehicle_number = vehicles_yard2
			elif request.form.get('YES') == 'enter_yard3' and arrivals_yard3 != None and arrivals_yard3 <= 3:
				vehicle_number = vehicles_yard3
			elif request.form.get('YES') == 'enter_SoCamSB1' and arrivals_SoCamSB1 != None and arrivals_SoCamSB1 <= 3:
				vehicle_number = vehicles_SoCamNB1
			elif request.form.get('YES') == 'enter_SoCamSB2' and arrivals_SoCamSB2 != None and arrivals_SoCamSB2 <= 3:
				vehicle_number = vehicles_SoCamSB2
			elif request.form.get('YES') == 'enter_SoCamSB3' and arrivals_SoCamSB2 != None and arrivals_SoCamSB3 <= 3:
				vehicle_number = vehicles_SoCamSB3
			elif request.form.get('YES') == 'enter_redoak1' and arrivals_redoak1 != None and arrivals_redoak1 <= 3:
				vehicle_number = vehicles_redoak1
			elif request.form.get('YES') == 'enter_redoak2' and arrivals_redoak2 != None and arrivals_redoak2 <= 3:
				vehicle_number = vehicles_redoak2
			elif request.form.get('YES') == 'enter_redoak3' and arrivals_redoak3 != None and arrivals_redoak3 <= 3:
				vehicle_number = vehicles_redoak3
			elif request.form.get('YES') == 'enter_lipman1' and arrivals_lipman1 != None and arrivals_lipman1 <= 3:
				vehicle_number = vehicles_lipman1
			elif request.form.get('YES') == 'enter_lipman2' and arrivals_lipman2 != None and arrivals_lipman2 <= 3:
				vehicle_number = vehicles_lipman2
			elif request.form.get('YES') == 'enter_lipman3' and arrivals_lipman3 != None and arrivals_lipman3 <= 3:
				vehicle_number = vehicles_lipman3
			elif request.form.get('YES') == 'enter_biel1'  and arrivals_biel1 != None and arrivals_biel1 <= 3:
				vehicle_number = vehicles_biel1
			elif request.form.get('YES') == 'enter_biel2' and arrivals_biel2 != None and arrivals_biel2 <= 3:
				vehicle_number = vehicles_biel2
			elif request.form.get('YES') == 'enter_biel3' and arrivals_biel3 != None and arrivals_biel3 <= 3:
				vehicle_number = vehicles_biel3
			elif request.form.get('YES') == 'enter_henderson1' and arrivals_henderson1 != None and arrivals_henderson1 <= 3:
				vehicle_number = vehicles_henderson1
			elif request.form.get('YES') == 'enter_henderson2' and arrivals_henderson2 != None and arrivals_henderson2 <= 3:
				vehicle_number = vehicles_henderson2
			elif request.form.get('YES') == 'enter_henderson3' and arrivals_henderson3 != None and arrivals_henderson3 <= 3:
				vehicle_number = vehicles_henderson3
			elif request.form.get('YES') == 'enter_gibbons1' and arrivals_gibbons1 != None and arrivals_gibbons1 <= 3:
				vehicle_number = vehicles_gibbons1
			elif request.form.get('YES') == 'enter_gibbons2' and arrivals_gibbons2 != None and arrivals_gibbons2 <= 3:
				vehicle_number = vehicles_gibbons2
			elif request.form.get('YES') == 'enter_gibbons3' and arrivals_gibbons3 != None and arrivals_gibbons3 <= 3:
				vehicle_number = vehicles_gibbons3
			elif request.form.get('YES') == 'enter_collegehall1' and arrivals_collegehall1 != None and arrivals_collegehall1 <= 3:
				vehicle_number = vehicles_collegehall1
			elif request.form.get('YES') == 'enter_collegehall2' and arrivals_collegehall2 != None and arrivals_collegehall2 <= 3:
				vehicle_number = vehicles_collegehall2
			elif request.form.get('YES') == 'enter_collegehall3' and arrivals_collegehall3 != None and arrivals_collegehall3 <= 3:
				vehicle_number = vehicles_collegehall3
			elif request.form.get('YES') == 'enter_SoCamNB1' and arrivals_SoCamNB1 != None and arrivals_SoCamNB1 <= 3:
				vehicle_number = vehicles_SoCamNB1
			elif request.form.get('YES') == 'enter_SoCamNB2' and arrivals_SoCamNB2 != None and arrivals_SoCamNB2 <= 3:
				vehicle_number = vehicles_SoCamNB2
			elif request.form.get('YES') == ' enter_SoCamNB3' and arrivals_SoCamNB3 != None and arrivals_SoCamNB3 <= 3:
				vehicle_number = vehicles_SoCamNB3
			elif request.form.get('YES') == 'enter_SACN1' and arrivals_SACN1 != None and arrivals_SACN1 <= 3:
				vehicle_number = vehicles_SACN1
			elif request.form.get('YES') == 'enter_SACN2' and arrivals_SACN2 != None and arrivals_SACN2 <= 3:
				vehicle_number = vehicles_SACN2
			elif request.form.get('YES') == 'enter_SACN3' and arrivals_SACN3 != None and arrivals_SACN3 <= 3:
				vehicle_number = vehicles_SACN3
			else:
				return redirect(url_for('EEBus'))

			session['current_bus'] = vehicle_number
			session['current_time'] = datetime.now().strftime("%H:%M:%S")
			session['current_route'] = 'Route EE'

			return redirect(url_for('exit_bus'))

	return render_template("EEBus.html",
						   arrivals_CASC1=arrivals_CASC1,
						   arrivals_CASC2=arrivals_CASC2,
						   arrivals_CASC3=arrivals_CASC3,

						   arrivals_yard1=arrivals_yard1,
						   arrivals_yard2=arrivals_yard2,
						   arrivals_yard3=arrivals_yard3,

						   arrivals_SoCamSB1=arrivals_SoCamSB1,
						   arrivals_SoCamSB2=arrivals_SoCamSB2,
						   arrivals_SoCamSB3=arrivals_SoCamSB3,

						   arrivals_redoak1=arrivals_redoak1,
						   arrivals_redoak2=arrivals_redoak2,
						   arrivals_redoak3=arrivals_redoak3,

						   arrivals_lipman1=arrivals_lipman1,
						   arrivals_lipman2=arrivals_lipman2,
						   arrivals_lipman3=arrivals_lipman3,

						   arrivals_biel1=arrivals_biel1,
						   arrivals_biel2=arrivals_biel2,
						   arrivals_biel3=arrivals_biel3,

						   arrivals_henderson1=arrivals_henderson1,
						   arrivals_henderson2=arrivals_henderson2,
						   arrivals_henderson3=arrivals_henderson3,

						   arrivals_gibbons1=arrivals_gibbons1,
						   arrivals_gibbons2=arrivals_gibbons2,
						   arrivals_gibbons3=arrivals_gibbons3,

						   arrivals_collegehall1=arrivals_collegehall1,
						   arrivals_collegehall2=arrivals_collegehall2,
						   arrivals_collegehall3=arrivals_collegehall3,

						   arrivals_SoCamNB1=arrivals_SoCamNB1,
						   arrivals_SoCamNB2=arrivals_SoCamNB2,
						   arrivals_SoCamNB3=arrivals_SoCamNB3,

						   arrivals_SACN1=arrivals_SACN1,
						   arrivals_SACN2=arrivals_SACN2,
						   arrivals_SACN3=arrivals_SACN3,

						   capacity=capacity)

@app.route("/F-bus", methods=['POST', 'GET'])
def FBus():
	if 'user_id' not in session:
		return redirect(url_for('login'))

	else:
		if 'current_bus' in session:
			session.pop('current_bus', None)
			session.pop('current_time', None)
			session.pop('current_route', None)

		capacity = c.execute("SELECT capacity FROM VEHICLES WHERE ID = 1").fetchone()
		capacity = capacity[0]
		#capacity = 0

		arrivals_CASC1, arrivals_CASC2, arrivals_CASC3, vehicles_CASC1, vehicles_CASC2, vehicles_CASC3 = route_vehicles('4015038', '4259014')
		arrivals_yard1, arrivals_yard2, arrivals_yard3, vehicles_yard1, vehicles_yard2, vehicles_yard3 = route_vehicles('4015038', '4229620')
		arrivals_redoak1, arrivals_redoak2, arrivals_redoak3, vehicles_redoak1, vehicles_redoak2, vehicles_redoak3 = route_vehicles('4015038', '4259030')
		arrivals_lipman1, arrivals_lipman2, arrivals_lipman3, vehicles_lipman1, vehicles_lipman2, vehicles_lipman3 = route_vehicles('4015038', '4229596')
		arrivals_biel1, arrivals_biel2, arrivals_biel3, vehicles_biel1, vehicles_biel2, vehicles_biel3 = route_vehicles('4015038', '4259054')
		arrivals_henderson1, arrivals_henderson2, arrivals_henderson3, vehicles_henderson1, vehicles_henderson2, vehicles_henderson3 = route_vehicles('4015038', '4259722')
		arrivals_gibbons1, arrivals_gibbons2, arrivals_gibbon3, vehicles_gibbon1, vehicles_gibbon2, vehicles_gibbon3 = route_vehicles('4015038', '4259058')
		arrivals_collegehall1, arrivals_collegehall2, arrivals_collegehall3, vehicles_collegehall1, vehicles_collegehall2, vehicles_collegehall3 = route_vehicles('4015038', '4253700')
		arrivals_SACN1, arrivals_SACN2, arrivals_SACN3, vehicles_SACN1, vehicles_SACN2, vehicles_SACN3 = route_vehicles('4015038', '4229496')

		print(type(arrivals_CASC1))
		if request.method == 'POST':
			if request.form.get('YES') == 'enter_CASC1' and arrivals_CASC1 != None and arrivals_CASC1 <= 3:
				vehicle_number = vehicles_CASC1
			elif request.form.get('YES') == 'enter_CASC2' and arrivals_CASC2 != None and arrivals_CASC2 <= 3:
				vehicle_number = vehicles_CASC2
			elif request.form.get('YES') == 'enter_CASC3' and arrivals_CASC3 != None and arrivals_CASC3 <= 3:
				vehicle_number = vehicles_CASC3
			elif request.form.get('YES') == 'enter_yard1' and arrivals_yard1 != None and arrivals_yard1 <= 3:
				vehicle_number = vehicles_yard1
			elif request.form.get('YES') == 'enter_yard2' and arrivals_yard2 != None and arrivals_yard2 <= 3:
				vehicle_number = vehicles_yard2
			elif request.form.get('YES') == 'enter_yard3' and arrivals_yard3 != None and arrivals_yard3 <= 3:
				vehicle_number == vehicles_yard3
			elif request.form.get('YES') == 'enter_redoak1' and arrivals_redoak1 != None and arrivals_redoak1 <=3:
				vehicle_number = vehicles_redoak1
			elif request.form.get('YES') == 'enter_redoak2' and arrivals_redoak2 != None and arrivals_redoak2 <= 3:
				vehicle_number = vehicles_redoak2
			elif request.form.get('YES') == 'enter_redoak3' and arrivals_redoak3 != None and arrivals_redoak3 <= 3:
				vehicle_number = vehicles_redoak3
			elif request.form.get('YES') == 'enter_lipman1' and arrivals_lipman1 != None and arrivals_lipman1 <= 3:
				vehicle_number = vehicles_lipman1
			elif request.form.get('YES') == 'enter_lipman2' and arrivals_lipman2 != None and arrivals_lipman2 <= 3:
				vehicle_number = vehicles_lipman2
			elif request.form.get('YES') == 'enter_lipman3' and arrivals_lipman3 != None and arrivals_lipman3 <= 3:
				vehicle_number = vehicles_lipman3
			elif request.form.get('YES') == 'enter_biel1' and arrivals_biel1 != None and arrivals_biel1 <= 3:
				vehicle_number = vehicles_biel1
			elif request.form.get('YES') == 'enter_biel2' and arrivals_biel2 != None and arrivals_biel2 <= 3:
				vehicle_number = vehicles_biel2
			elif request.form.get('YES') == 'enter_biel3' and arrivals_biel3 != None and arrivals_biel3 <= 3:
				vehicle_number = vehicles_biel3
			elif request.form.get('YES') == 'enter_henderson1' and arrivals_henderson1 != None and arrivals_henderson1 <= 3:
				vehicle_number = vehicles_henderson1
			elif request.form.get('YES') == 'enter_henderson2' and arrivals_henderson2 != None and arrivals_henderson2 <= 3:
				vehicle_number = vehicles_henderson2
			elif request.form.get('YES') == 'enter_henderson3' and arrivals_henderson3 != None and arrivals_henderson3 <= 3:
				vehicles_number = vehicles_henderson3
			elif request.form.get('YES') == 'enter_gibbons1' and arrivals_gibbons1 != None and arrivals_gibbons1 <= 3:
				vehicle_number = vehicles_gibbon1
			elif request.form.get('YES') == 'enter_gibbons2' and arrivals_gibbons2 != None and arrivals_gibbons2 <= 3:
				vehicle_number = vehicles_gibbon2
			elif request.form.get('YES') == 'enter_gibbons3' and arrivals_gibbon3 != None and arrivals_gibbon3 <= 3:
				vehicle_number = vehicles_gibbon3
			elif request.form.get('YES') == 'enter_collegehall1' and arrivals_collegehall1 != None and arrivals_collegehall1 <= 3:
				vehicle_number = vehicles_collegehall1
			elif request.form.get('YES') == 'enter_collegehall2' and arrivals_collegehall2 != None and arrivals_collegehall2 <= 3:
				vehicle_number = vehicles_collegehall2
			elif request.form.get('YES') == 'enter_collegehall3' and arrivals_collegehall3 != None and arrivals_collegehall3 <= 3:
				vehicle_number = vehicles_collegehall3
			elif request.form.get('YES') == 'enter_SACN1' and arrivals_SACN1 != None and arrivals_SACN1 <= 3:
				vehicle_number = vehicles_SACN1
			elif request.form.get('YES') == 'enter_SACN2' and arrivals_SACN2 != None and arrivals_SACN2 <= 3:
				vehicle_number = vehicles_SACN2
			elif request.form.get('YES') == 'enter_SACN3' and arrivals_SACN3 != None and arrivals_SACN3 <= 3:
				vehicle_number = vehicles_SACN3
			else:
				return redirect(url_for('FBus'))

			session['current_bus'] = vehicle_number
			session['current_time'] = datetime.now().strftime("%H:%M:%S")
			session['current_route'] = 'Route F'

			return redirect(url_for('exit_bus'))

	return render_template("FBus.html",
						   arrivals_CASC1=arrivals_CASC1,
						   arrivals_CASC2=arrivals_CASC2,
						   arrivals_CASC3=arrivals_CASC3,

						   arrivals_yard1=arrivals_yard1,
						   arrivals_yard2=arrivals_yard2,
						   arrivals_yard3=arrivals_yard3,

						   arrivals_redoak1=arrivals_redoak1,
						   arrivals_redoak2=arrivals_redoak2,
						   arrivals_redoak3=arrivals_redoak3,

						   arrivals_lipman1=arrivals_lipman1,
						   arrivals_lipman2=arrivals_lipman2,
						   arrivals_lipman3=arrivals_lipman3,

						   arrivals_biel1=arrivals_biel1,
						   arrivals_biel2=arrivals_biel2,
						   arrivals_biel3=arrivals_biel3,

						   arrivals_henderson1=arrivals_henderson1,
						   arrivals_henderson2=arrivals_henderson2,
						   arrivals_henderson3=arrivals_henderson3,

						   arrivals_gibbons1=arrivals_gibbons1,
						   arrivals_gibbons2=arrivals_gibbons2,
						   arrivals_gibbon3=arrivals_gibbon3,

						   arrivals_collegehall1=arrivals_collegehall1,
						   arrivals_collegehall2=arrivals_collegehall2,
						   arrivals_collegehall3=arrivals_collegehall3,

						   arrivals_SACN1=arrivals_SACN1,
						   arrivals_SACN2=arrivals_SACN2,
						   arrivals_SACN3=arrivals_SACN3,

						   capacity=capacity)

@app.route("/H-bus", methods=['POST', 'GET'])
def HBus():
	if 'user_id' not in session:
		return redirect(url_for('login'))
	else:

		if 'current_bus' in session:
			session.pop('current_bus', None)
			session.pop('current_time', None)
			session.pop('current_route', None)

		capacity = c.execute("SELECT capacity FROM VEHICLES WHERE ID = 1").fetchone()
		capacity = capacity[0]

		#capacity = 0

		arrivals_BSC1, arrivals_BSC2, arrivals_BSC3, vehicles_BSC1, vehicles_BSC2, vehicles_BSC3 = route_vehicles('4015030', '4259062')
		arrivals_allison1, arrivals_allison2, arrivals_allison3, vehicles_allison1, vehicles_allison2, vehicles_allison3 = route_vehicles('4015030', '4259048')
		arrivals_hill1, arrivals_hill2, arrivals_hill3, vehicles_hill1, vehicles_hill2, vehicles_hill3 = route_vehicles('4015030', '4231636')
		arrivals_stadium1, arrivals_stadium2, arrivals_stadium3, vehicles_stadium1, vehicles_stadium2, vehicles_stadium3 = route_vehicles('4015030', '4259010')
		arrivals_CASC1, arrivals_CASC2, arrivals_CASC3, vehicles_CASC1, vehicles_CASC2, vehicles_CASC3 = route_vehicles('4015030', '4259014')
		arrivals_yard1, arrivals_yard2, arrivals_yard3, vehicles_yard1, vehicles_yard2, vehicles_yard3 = route_vehicles('4015030', '4229620')
		arrivals_SACN1, arrivals_SACN2, arrivals_SACN3, vehicles_SACN1, vehicles_SACN2, vehicles_SACN3 = route_vehicles('4015030', '4229496')
		arrivals_werblin1, arrivals_werblin2, arrivals_werblin3, vehicles_werblin1, vehicles_werblin2, vehicles_werblin3 = route_vehicles('4015030', '4259040')

		if request.method == 'POST':
			if request.form.get('YES') == 'enter_BSC1' and arrivals_BSC1 != None and arrivals_BSC1 <= 3:
				vehicle_number = vehicles_BSC1
			elif request.form.get('YES') == 'enter_BSC2' and arrivals_BSC2 != None and arrivals_BSC2 <= 3:
				vehicle_number = vehicles_BSC2
			elif request.form.get('YES') == 'enter_BSC3' and arrivals_BSC3 != None and arrivals_BSC3 <= 3:
				vehicle_number = vehicles_BSC3
			elif request.form.get('YES') == 'enter_arc1' and arrivals_allison1 != None and arrivals_allison1 <= 3:
				vehicle_number = vehicles_allison1
			elif request.form.get('YES') == 'enter_arc2' and arrivals_allison2 != None and arrivals_allison2 <= 3:
				vehicle_number = vehicles_allison2
			elif request.form.get('YES') == 'enter_arc3' and arrivals_allison3 != None and arrivals_allison3 <= 3:
				vehicle_number = vehicles_allison3
			elif request.form.get('YES') == 'enter_hillSB1' and arrivals_hill1 != None and arrivals_hill1 <= 3:
				vehicle_number = vehicles_hill1
			elif request.form.get('YES') == 'enter_hillSB2' and arrivals_hill2 != None and arrivals_hill2 <= 3:
				vehicle_number = vehicles_hill2
			elif request.form.get('YES') == 'enter_hillSB3' and arrivals_hill3 != None and arrivals_hill3 <= 3:
				vehicle_number = vehicles_hill3
			elif request.form.get('YES') == 'enter_stadium1' and arrivals_stadium1 != None and arrivals_stadium1 <= 3:
				vehicle_number = vehicles_stadium1
			elif request.form.get('YES') == 'enter_stadium2' and arrivals_stadium2 != None and arrivals_stadium2 <= 3:
				vehicle_number = vehicles_stadium2
			elif request.form.get('YES') == 'enter_stadium3' and arrivals_stadium3 != None and arrivals_stadium3 <= 3:
				vehicle_number = vehicles_stadium3
			elif request.form.get('YES') == 'enter_CASC1' and arrivals_CASC1 != None and arrivals_CASC1 <= 3:
				vehicle_number = vehicles_CASC1
			elif request.form.get('YES') == 'enter_CASC2' and arrivals_CASC2 != None and arrivals_CASC2 <= 3:
				vehicle_number = vehicles_CASC1
			elif request.form.get('YES') == 'enter_CASC3' and arrivals_CASC3 != None and arrivals_CASC3 <= 3:
				vehicle_number = vehicles_CASC3
			elif request.form.get('YES') == 'enter_yard1' and arrivals_yard1 != None and arrivals_yard1 <= 3:
				vehicle_number = vehicles_yard1
			elif request.form.get('YES') == 'enter_yard2' and arrivals_yard2 != None and arrivals_yard2 <= 3:
				vehicle_number = vehicles_yard2
			elif request.form.get('YES') == 'enter_yard3' and arrivals_yard3 != None and arrivals_yard3 <= 3:
				vehicle_number = vehicles_yard3
			elif request.form.get('YES') == 'enter_SACN1' and arrivals_SACN1 != None and arrivals_SACN1 <= 3:
				vehicle_number = vehicles_SACN1
			elif request.form.get('YES') == 'enter_SACN2' and arrivals_SACN2 != None and arrivals_SACN2 <= 3:
				vehicle_number = vehicles_SACN2
			elif request.form.get('YES') == 'enter_SACN3' and arrivals_SACN3 != None and arrivals_SACN3 <= 3:
				vehicle_number = vehicles_SACN3
			elif request.form.get('YES') == 'enter_werblin1' and arrivals_werblin1 != None and arrivals_werblin1 <= 3:
				vehicle_number = vehicles_werblin1
			elif request.form.get('YES') == 'enter_werblin2' and arrivals_werblin2 != None and arrivals_werblin2 <= 3:
				vehicle_number = vehicles_werblin2
			elif request.form.get('YES') == 'enter_werblin3' and arrivals_werblin3 != None and arrivals_werblin3 <= 3:
				vehicle_number = vehicles_werblin3
			else:
				return redirect(url_for('HBus'))

			session['current_bus'] = vehicle_number
			session['current_time'] = datetime.now().strftime("%H:%M:%S")
			session['current_route'] = 'Route H'

			return redirect(url_for('exit_bus'))

	return render_template("HBus.html",
						   arrivals_BSC1=arrivals_BSC1,
						   arrivals_BSC2=arrivals_BSC2,
						   arrivals_BSC3=arrivals_BSC3,

						   arrivals_allison1=arrivals_allison1,
						   arrivals_allison2=arrivals_allison2,
						   arrivals_allison3=arrivals_allison3,

						   arrivals_hill1=arrivals_hill1,
						   arrivals_hill2=arrivals_hill2,
						   arrivals_hill3=arrivals_hill3,

						   arrivals_stadium1=arrivals_stadium1,
						   arrivals_stadium2=arrivals_stadium2,
						   arrivals_stadium3=arrivals_stadium3,

						   arrivals_CASC1=arrivals_CASC1,
						   arrivals_CASC2=arrivals_CASC2,
						   arrivals_CASC3=arrivals_CASC3,

						   arrivals_yard1=arrivals_yard1,
						   arrivals_yard2=arrivals_yard2,
						   arrivals_yard3=arrivals_yard3,

						   arrivals_SACN1=arrivals_SACN1,
						   arrivals_SACN2=arrivals_SACN2,
						   arrivals_SACN3=arrivals_SACN3,

						   arrivals_werblin1=arrivals_werblin1,
						   arrivals_werblin2=arrivals_werblin2,
						   arrivals_werblin3=arrivals_werblin3,

						   capacity=capacity
						   )

@app.route("/LX-bus", methods=['POST', 'GET'])
def LXBus():
	if 'user_id' not in session:
		return redirect(url_for('login'))
	else:

		if 'current_bus' in session:
			session.pop('current_bus', None)
			session.pop('current_time', None)
			session.pop('current_route', None)

		capacity = c.execute("SELECT capacity FROM VEHICLES WHERE ID = 1").fetchone()
		capacity = capacity[0]
		#capacity = 0

		arrivals_LSC1, arrivals_LSC2, arrivals_LSC3, vehicles_LSC1, vehicles_LSC2, vehicles_LSC3 = route_vehicles('4015040', '4254110')
		arrivals_CASC1, arrivals_CASC2, arrivals_CASC3, vehicles_CASC1, vehicles_CASC2, vehicles_CASC3 = route_vehicles('4015040', '4259014')
		arrivals_yard1, arrivals_yard2, arrivals_yard3, vehicles_yard1, vehicles_yard2, vehicles_yard3 = route_vehicles('4015040', '4229620')
		arrivals_SACN1, arrivals_SACN2, arrivals_SACN3, vehicles_SACN1, vehicles_SACN2, vehicles_SACN3 = route_vehicles('4015040', '4229496')
		arrivals_livi1, arrivals_livi2, arrivals_livi3, vehicles_livi1, vehicles_livi2, vehicles_livi3 = route_vehicles('4015040', '4229570')

		if request.method == 'POST':
			if request.form.get('YES') == 'enter_LSC1' and arrivals_LSC1 != None and arrivals_LSC1 <= 3:
				vehicle_number = vehicles_LSC1
			elif request.form.get('YES') == 'enter_LSC2' and arrivals_LSC2 != None and arrivals_LSC2 <= 3:
				vehicle_number = vehicles_LSC2
			elif request.form.get('YES') == 'enter_LSC3' and arrivals_LSC3 != None and arrivals_LSC3 <= 3:
				vehicle_number = vehicles_LSC3
			elif request.form.get('YES') == 'enter_CASC1' and arrivals_CASC1 != None and arrivals_CASC1 <= 3:
				vehicle_number = vehicles_CASC1
			elif request.form.get('YES') == 'enter_CASC2' and arrivals_CASC2 != None and arrivals_CASC2 <= 3:
				vehicle_number = vehicles_CASC2
			elif request.form.get('YES') == 'enter_CASC3' and arrivals_CASC3 != None and arrivals_CASC3 <= 3:
				vehicle_number = vehicles_CASC3
			elif request.form.get('YES') == 'enter_yard1' and arrivals_yard1 != None and arrivals_yard1 <= 3:
				vehicle_number = vehicles_yard1
			elif request.form.get('YES') == 'enter_yard2' and arrivals_yard2 != None and arrivals_yard2 <= 3:
				vehicle_number = vehicles_yard2
			elif request.form.get('YES') == 'enter_yard3' and arrivals_yard3 != None and arrivals_yard3 <= 3:
				vehicle_number = vehicles_yard3
			elif request.form.get('YES') == 'enter_SACN1' and arrivals_SACN1 != None and arrivals_SACN1 <= 3:
				vehicle_number = vehicles_SACN1
			elif request.form.get('YES') == 'enter_SACN2' and arrivals_SACN2 != None and arrivals_SACN2 <= 3:
				vehicle_number = vehicles_SACN2
			elif request.form.get('YES') == 'enter_SACN3' and arrivals_SACN3 != None and arrivals_SACN3 <= 3:
				vehicle_number = vehicles_SACN3
			elif request.form.get('YES') == 'enter_livi1' and arrivals_livi1 != None and arrivals_livi1 <= 3:
				vehicle_number = vehicles_livi1
			elif request.form.get('YES') == 'enter_livi2' and arrivals_livi2 != None and arrivals_livi2 <= 3:
				vehicle_number = vehicles_livi2
			elif request.form.get('YES') == 'enter_livi3' and arrivals_livi3 != None and arrivals_livi3 <= 3:
				vehicle_number = vehicles_livi3
			else:
				return redirect(url_for('LXBus'))

			session['current_bus'] = vehicle_number
			session['current_time'] = datetime.now().strftime("%H:%M:%S")
			session['current_route'] = 'Route LX'

			return redirect(url_for('exit_bus'))
	return render_template("LXBus.html",
						   arrivals_LSC1=arrivals_LSC1,
						   arrivals_LSC2=arrivals_LSC2,
						   arrivals_LSC3=arrivals_LSC3,

						   arrivals_CASC1=arrivals_CASC1,
						   arrivals_CASC2=arrivals_CASC2,
						   arrivals_CASC3=arrivals_CASC3,

						   arrivals_yard1=arrivals_yard1,
						   arrivals_yard2=arrivals_yard2,
						   arrivals_yard3=arrivals_yard3,

						   arrivals_SACN1=arrivals_SACN1,
						   arrivals_SACN2=arrivals_SACN2,
						   arrivals_SACN3=arrivals_SACN3,

						   arrivals_livi1=arrivals_livi1,
						   arrivals_livi2=arrivals_livi2,
						   arrivals_livi3=arrivals_livi3,

						   capacity=capacity
						   )

@app.route("/REXL-bus", methods=['POST', 'GET'])
def REXLBus():
	if 'user_id' not in session:
		return redirect(url_for('login'))
	else:
		if 'current_bus' in session:
			session.pop('current_bus', None)
			session.pop('current_time', None)
			session.pop('current_route', None)

		capacity = c.execute("SELECT capacity FROM VEHICLES WHERE ID = 1").fetchone()
		capacity = capacity[0]
		#capacity = 0

		arrivals_redoak1, arrivals_redoak2, arrivals_redoak3, vehicles_redoak1, vehicles_redoak2, vehicles_redoak3 = route_vehicles('4015044', '4259030')
		arrivals_lipman1, arrivals_lipman2, arrivals_lipman3, vehicles_lipman1, vehicles_lipman2, vehicles_lipman3 = route_vehicles('4015044', '4229596')
		arrivals_collegehall1, arrivals_collegehall2, arrivals_collegehall3, vehicles_collegehall1, vehicles_collegehall2, vehicles_collegehall3 = route_vehicles('4015044', '4253700')
		arrivals_livi1, arrivals_livi2, arrivals_livi3, vehicles_livi1, vehicles_livi2, vehicles_livi3 = route_vehicles('4015044', '4229570')
		arrivals_LSC1, arrivals_LSC2, arrivals_LSC3, vehicles_LSC1, vehicles_LSC2, vehicles_LSC3 = route_vehicles('4015044', '4254110')

		if request.method == 'POST':
			if request.form.get('YES') == 'enter_redoak1' and arrivals_redoak1 != None and arrivals_redoak1 <= 3:
				vehicle_number = vehicles_redoak1
			elif request.form.get('YES') == 'enter_redoak2' and arrivals_redoak2 != None and arrivals_redoak2 <= 3:
				vehicle_number = vehicles_redoak2
			elif request.form.get('YES') == 'enter_redoak3' and arrivals_redoak3 != None and arrivals_redoak3 <= 3:
				vehicle_number = vehicles_redoak3
			elif request.form.get('YES') == 'enter_lipman1' and arrivals_lipman1 != None and arrivals_lipman1 <= 3:
				vehicle_number = vehicles_lipman1
			elif request.form.get('YES') == 'enter_lipman2' and arrivals_lipman2 != None and arrivals_lipman2 <= 3:
				vehicle_number = vehicles_lipman2
			elif request.form.get('YES') == 'enter_lipman3' and arrivals_lipman3 != None and arrivals_lipman3 <= 3:
				vehicle_number = vehicles_lipman3
			elif request.form.get('YES') == 'enter_collegehall1' and arrivals_collegehall1 != None and arrivals_collegehall1 <= 3:
				vehicle_number = vehicles_collegehall1
			elif request.form.get('YES') == 'enter_collegehall2' and arrivals_collegehall2 != None and arrivals_collegehall2 <= 3:
				vehicle_number = vehicles_collegehall2
			elif request.form.get('YES') == 'enter_collegehall3' and arrivals_collegehall3 != None and arrivals_collegehall3 <= 3:
				vehicle_number = vehicles_collegehall3
			elif request.form.get('YES') == 'enter_livi1' and arrivals_livi1 != None and arrivals_livi1 <= 3:
				vehicle_number = vehicles_livi1
			elif request.form.get('YES') == 'enter_livi2' and arrivals_livi2 != None and arrivals_livi2 <= 3:
				vehicle_number = vehicles_livi2
			elif request.form.get('YES') == 'enter_livi3' and arrivals_livi3 != None and arrivals_livi3 <= 3:
				vehicle_number = vehicles_livi3
			elif request.form.get('YES') == 'enter_LSC1' and arrivals_LSC1 != None and arrivals_LSC1 <= 3:
				vehicle_number = vehicles_LSC1
			elif request.form.get('YES') == 'enter_LSC2' and arrivals_LSC2 != None and arrivals_LSC2 <= 3:
				vehicle_number = vehicles_LSC2
			elif request.form.get('YES') == 'enter_LSC3' and arrivals_LSC3 != None and arrivals_LSC3 <= 3:
				vehicle_number = vehicles_LSC3
			else:
				return redirect(url_for('REXLBus'))

			session['current_bus'] = vehicle_number
			session['current_time'] = datetime.now().strftime("%H:%M:%S")
			session['current_route'] = 'Route REXL'

			return redirect(url_for('exit_bus'))

	return render_template("REXLBus.html",
						   arrivals_redoak1=arrivals_redoak1,
						   arrivals_redoak2=arrivals_redoak2,
						   arrivals_redoak3=arrivals_redoak3,

						   arrivals_lipman1=arrivals_lipman1,
						   arrivals_lipman2=arrivals_lipman2,
						   arrivals_lipman3=arrivals_lipman3,

						   arrivals_collegehall1=arrivals_collegehall1,
						   arrivals_collegehall2=arrivals_collegehall2,
						   arrivals_collegehall3=arrivals_collegehall3,

						   arrivals_livi1=arrivals_livi1,
						   arrivals_livi2=arrivals_livi2,
						   arrivals_livi3=arrivals_livi3,

						   arrivals_LSC1=arrivals_LSC1,
						   arrivals_LSC2=arrivals_LSC2,
						   arrivals_LSC3=arrivals_LSC3,

						   capacity=capacity
						   )

@app.route("/REXB-bus", methods=['POST', 'GET'])
def REXBBus():
	if 'user_id' not in session:
		return redirect(url_for('login'))
	else:

		if 'current_bus' in session:
			session.pop('current_bus', None)
			session.pop('current_time', None)
			session.pop('current_route', None)

		capacity = c.execute("SELECT capacity FROM VEHICLES WHERE ID = 1").fetchone()
		capacity = capacity[0]
		#capacity = 0

		arrivals_redoak1, arrivals_redoak2, arrivals_redoak3, vehicles_redoak1, vehicles_redoak2, vehicles_redoak3 = route_vehicles('4015042','4259030')
		arrivals_lipman1, arrivals_lipman2, arrivals_lipman3, vehicles_lipman1, vehicles_lipman2, vehicles_lipman3 = route_vehicles('4015042','4229596')
		arrivals_collegehall1, arrivals_collegehall2, arrivals_collegehall3, vehicles_collegehall1, vehicles_collegehall2, vehicles_collegehall3 = route_vehicles('4015042', '4253700')
		arrivals_hillNB1, arrivals_hillNB2, arrivals_hillNB3, vehicles_hillNB1, vehicles_hillNB2, vehicles_hillNB3 = route_vehicles('4015042','4259016')
		arrivals_allison1, arrivals_allison2, arrivals_allison3, vehicles_allison1, vehicles_allison2, vehicles_allison3 = route_vehicles('4015042','4259048')
		arrivals_hillSB1, arrivals_hillSB2, arrivals_hillSB3, vehicles_hillSB1, vehicles_hillSB2, vehicles_hillSB3 = route_vehicles('4015042','4231636')

		if request.method == 'POST':
			if request.form.get('YES') == 'enter_redoak1' and arrivals_redoak1 != None and arrivals_redoak1 <= 3:
				vehicle_number = vehicles_redoak1
			elif request.form.get('YES') == 'enter_redoak2' and arrivals_redoak2 != None and arrivals_redoak2 <= 3:
				vehicle_number = vehicles_redoak2
			elif request.form.get('YES') == 'enter_redoak3' and  arrivals_redoak3 != None and arrivals_redoak3 <= 3:
				vehicle_number = vehicles_redoak3
			elif request.form.get('YES') == 'enter_lipman1' and arrivals_lipman1 != None and arrivals_lipman1 <= 3:
				vehicle_number = vehicles_lipman1
			elif request.form.get('YES') == 'enter_lipman2' and arrivals_lipman2 != None and arrivals_lipman2 <= 3:
				vehicle_number = vehicles_lipman2
			elif request.form.get('YES') == 'enter_lipman3' and arrivals_lipman3 != None and arrivals_lipman3 <= 3:
				vehicle_number = vehicles_lipman3
			elif request.form.get('YES') == 'enter_collegehall1' and arrivals_collegehall1 != None and arrivals_collegehall1 <= 3:
				vehicle_number = vehicles_collegehall1
			elif request.form.get('YES') == 'enter_collegehall2' and arrivals_collegehall2 != None and arrivals_collegehall2 <= 3:
				vehicle_number = vehicles_collegehall2
			elif request.form.get('YES') == 'enter_college_hall3' and arrivals_collegehall3 != None and arrivals_collegehall3 <= 3:
				vehicle_number = vehicles_collegehall3
			elif request.form.get('YES') == 'enter_hillNB1'  and arrivals_hillNB1 != None and arrivals_hillNB1 <= 3:
				vehicle_number = vehicles_hillNB1
			elif request.form.get('YES') == 'enter_hillNB2' and arrivals_hillNB2 != None and arrivals_hillNB2 <= 3:
				vehicle_number = vehicles_hillNB2
			elif request.form.get('YES') == 'enter_hillNB3' and arrivals_hillNB3 != None and arrivals_hillNB3 <= 3:
				vehicle_number = vehicles_hillNB3
			elif request.form.get('YES') == 'enter_arc1' and arrivals_allison1 != None and arrivals_allison1 <= 3:
				vehicle_number = vehicles_allison1
			elif request.form.get('YES') == 'enter_arc2' and arrivals_allison2 != None and arrivals_allison2 <= 3:
				vehicle_number = vehicles_allison2
			elif request.form.get('YES') == 'enter_arc3' and arrivals_allison3 != None and arrivals_allison3 <= 3:
				vehicle_number = vehicles_allison3
			elif request.form.get('YES') == 'enter_hillSB1' and arrivals_hillSB1 != None and arrivals_hillSB1 <= 3:
				vehicle_number = vehicles_hillSB1
			elif request.form.get('YES') == 'enter_hillSB2' and arrivals_hillSB2 != None and arrivals_hillSB2 <= 3:
				vehicle_number = vehicles_hillSB2
			elif request.form.get('YES') == 'enter_hillSB3' and arrivals_hillSB3 != None and arrivals_hillSB3 <= 3:
				vehicle_number = vehicles_hillSB3
			else:
				return redirect(url_for('REXBBus'))

			session['current_bus'] = vehicle_number
			session['current_time'] = datetime.now().strftime("%H:%M:%S")
			session['current_route'] = 'Route REXB'

			return redirect(url_for('exit_bus'))

	return render_template("REXBBus.html",
						   arrivals_redoak1=arrivals_redoak1,
						   arrivals_redoak2=arrivals_redoak2,
						   arrivals_redoak3=arrivals_redoak3,

						   arrivals_lipman1=arrivals_lipman1,
						   arrivals_lipman2=arrivals_lipman2,
						   arrivals_lipman3=arrivals_lipman3,

						   arrivals_collegehall1=arrivals_collegehall1,
						   arrivals_collegehall2=arrivals_collegehall2,
						   arrivals_collegehall3=arrivals_collegehall3,

						   arrivals_hillNB1=arrivals_hillNB1,
						   arrivals_hillNB2=arrivals_hillNB2,
						   arrivals_hillNB3=arrivals_hillNB3,

						   arrivals_allison1=arrivals_allison1,
						   arrivals_allison2=arrivals_allison2,
						   arrivals_allison3=arrivals_allison3,

						   arrivals_hillSB1=arrivals_hillSB1,
						   arrivals_hillSB2=arrivals_hillSB2,
						   arrivals_hillSB3=arrivals_hillSB3,

						   capacity=capacity
						   )

@app.route("/Weekend-2-bus", methods=['POST', 'GET'])
def weekendTwoBus():
	if 'user_id' not in session:
		return redirect(url_for('login'))
	else:

		if 'current_bus' in session:
			session.pop('current_bus', None)
			session.pop('current_time', None)
			session.pop('current_route', None)

		capacity = c.execute("SELECT capacity FROM VEHICLES WHERE ID = 1").fetchone()
		capacity = capacity[0]
		#capacity = 0

		arrivals_CAstudentctr1, arrivals_CAstudentctr2, arrivals_CAstudentctr3, vehicles_CAstudentctr1, vehicles_CAstudentctr2, vehicles_CAstudentctr3 = route_vehicles('4012652', '4259014')
		arrivals_yard1, arrivals_yard2, arrivals_yard3, vehicles_yard1, vehicles_yard2, vehicles_yard3 = route_vehicles('4012652', '4229620')
		arrivals_SoCam1, arrivals_SoCam2, arrivals_SoCam3, vehicles_SoCam1, vehicles_SoCam2, vehicles_SoCam3 = route_vehicles('4012652', '4259050')
		arrivals_redOak1, arrivals_redOak2, arrivals_redOak3, vehicles_redOak1, vehicles_redOak2, vehicles_redOak3 = route_vehicles('4012652', '4259030')
		arrivals_lipman1, arrivals_lipman2, arrivals_lipman3, vehicles_lipman1, vehicles_lipman2, vehicles_lipman3 = route_vehicles('4012652', '4229596')
		arrivals_biel1, arrivals_biel2, arrivals_biel3, vehicles_biel1, vehicles_biel2, vehicles_biel3 = route_vehicles('4012652', '4259054')
		arrivals_henderson1, arrivals_henderson2, arrivals_henderson3, vehicles_henderson1, vehicles_henderson2, vehicles_henderson3 = route_vehicles('4012652', '4259722')
		arrivals_gibbons1, arrivals_gibbons2, arrivals_gibbons3, vehicles_gibbons1, vehicles_gibbons2, vehicles_gibbons3 = route_vehicles('4012652', '4259058')
		arrivals_collgehall1, arrivals_collegehall2, arrivals_collegehall3, vehicles_collegehall1, vehicles_collegehall2, vehicles_collegehall3 = route_vehicles('4012652', '4253700')
		arrivals_SACN1, arrivals_SACN2, arrivals_SACN3, vehicles_SACN1, vehicles_SACN2, vehicles_SACN3 = route_vehicles('4012652', '4229496')
		arrivals_livi1, arrivals_livi2, arrivals_livi3, vehicles_livi1, vehicles_livi2, vehicles_livi3 = route_vehicles('4012652', '4229570')
		arrivals_LSC1, arrivals_LSC2, arrivals_LSC3, vehicles_LSC1, vehicles_LSC2, vehicles_LSC3 = route_vehicles('4012652', '4254110')
		arrivals_BSC1, arrivals_BSC2, arrivals_BSC3, vehicles_BSC1, vehicles_BSC2, vehicles_BSC3 = route_vehicles('4012652', '4259062')
		arrivals_allison1, arrivals_allison2, arrivals_allison3, vehicles_allison1, vehicles_allison2, vehicles_allison3 = route_vehicles('4012652', '4259048')
		arrivals_hill1, arrivals_hill2, arrivals_hill3, vehicles_hill1, vehicles_hill2, vehicles_hill3 = route_vehicles('4012652', '4231636')

		if request.method == 'POST':
			if request.form.get('YES') == 'enter_CASC1' and arrivals_CAstudentctr1 != None and arrivals_CAstudentctr1 <= 3:
				vehicle_number = vehicles_CAstudentctr1
			elif request.form.get('YES') == 'enter_CASC2' and arrivals_CAstudentctr2 != None and arrivals_CAstudentctr2 <= 3:
				vehicle_number = vehicles_CAstudentctr2
			elif request.form.get('YES') == 'enter_CASC3' and arrivals_CAstudentctr3 != None and arrivals_CAstudentctr3 <= 3:
				vehicle_number = vehicles_CAstudentctr3
			elif request.form.get('YES') == 'enter_yard1' and arrivals_yard1 != None and arrivals_yard1 <= 3:
				vehicle_number = vehicles_yard1
			elif request.form.get('YES') == 'enter_yard2' and arrivals_yard2 != None and arrivals_yard2 <= 3:
				vehicle_number = vehicles_yard2
			elif request.form.get('YES') == 'enter_yard3' and arrivals_yard3 != None and arrivals_yard3 <= 3:
				vehicle_number = vehicles_yard3
			elif request.form.get('YES') == 'enter_SoCam1' and arrivals_SoCam1 != None and arrivals_SoCam1 <= 3:
				vehicle_number = vehicles_SoCam1
			elif request.form.get('YES') == 'enter_SoCam2' and arrivals_SoCam2 != None and arrivals_SoCam2 <= 3:
				vehicle_number = vehicles_SoCam2
			elif request.form.get('YES') == 'enter_SoCam3' and arrivals_SoCam3 != None and arrivals_SoCam3 <= 3:
				vehicle_number = vehicles_SoCam3
			elif request.form.get('YES') == 'enter_redoak1' and arrivals_redOak1 != None and arrivals_redOak1 <= 3:
				vehicle_number = vehicles_redOak1
			elif request.form.get('YES') == 'enter_redoak2' and arrivals_redOak2 != None and arrivals_redOak2 <= 3:
				vehicle_number = vehicles_redOak2
			elif request.form.get('YES') == 'enter_redoak3' and arrivals_redOak3 != None and arrivals_redOak3 <= 3:
				vehicle_number = vehicles_redOak3
			elif request.form.get('YES') == 'enter_lipman1' and arrivals_lipman1 != None and arrivals_lipman1 <= 3:
				vehicle_number = vehicles_lipman1
			elif request.form.get('YES') == 'enter_lipman2' and arrivals_lipman2 != None and arrivals_lipman2 <= 3:
				vehicle_number = vehicles_lipman2
			elif request.form.get('YES') == 'enter_lipman3' and arrivals_lipman3 != None and arrivals_lipman3 <= 3:
				vehicle_number = vehicles_lipman3
			elif request.form.get('YES') == 'enter_biel1' and arrivals_biel1 != None and arrivals_biel1 <= 3:
				vehicle_number = vehicles_biel1
			elif request.form.get('YES') == 'enter_biel2' and arrivals_biel2 != None and arrivals_biel2 <= 3:
				vehicle_number = vehicles_biel2
			elif request.form.get('YES') == 'enter_biel3' and arrivals_biel3 != None and arrivals_biel3 <= 3:
				vehicle_number = vehicles_biel3
			elif request.form.get('YES') == 'enter_henderson1' and arrivals_henderson1 != None and arrivals_henderson1 <= 3:
				vehicle_number = vehicles_henderson1
			elif request.form.get('YES') == 'enter_henderson2' and arrivals_henderson2 != None and arrivals_henderson2 <= 3:
				vehicle_number = vehicles_henderson2
			elif request.form.get('YES') == 'enter_henderson3' and arrivals_henderson3 != None and arrivals_henderson3 <= 3:
				vehicle_number = vehicles_henderson3
			elif request.form.get('YES') == 'enter_gibbons1' and arrivals_gibbons1 != None and arrivals_gibbons1 <= 3:
				vehicle_number = vehicles_gibbons1
			elif request.form.get('YES') == 'enter_gibbons2' and arrivals_gibbons2 != None and arrivals_gibbons2 <= 3:
				vehicle_number = vehicles_gibbons2
			elif request.form.get('YES') == 'enter_gibbons3' and arrivals_gibbons3 != None and arrivals_gibbons3 <= 3:
				vehicle_number = vehicles_gibbons3
			elif request.form.get('YES') == 'enter_collegehall1' and arrivals_collgehall1 != None and arrivals_collgehall1 <= 3:
				vehicle_number = vehicles_collegehall1
			elif request.form.get('YES') == 'enter_collegehall2' and arrivals_collegehall2 != None and arrivals_collegehall2 <= 3:
				vehicle_number = vehicles_collegehall2
			elif request.form.get('YES') == 'enter_collegehall3' and arrivals_collegehall3 != None and arrivals_collegehall3 <= 3:
				vehicle_number = vehicles_collegehall3
			elif request.form.get('YES') == 'enter_SACN1' and arrivals_SACN1 != None and arrivals_SACN1 <= 3:
				vehicle_number = vehicles_SACN1
			elif request.form.get('YES') == 'enter_SACN2' and arrivals_SACN2 != None and arrivals_SACN2 <= 3:
				vehicle_number = vehicles_SACN2
			elif request.form.get('YES') == 'enter_SACN3' and arrivals_SACN3 != None and arrivals_SACN3 <= 3:
				vehicle_number = vehicles_SACN3
			elif request.form.get('YES') == 'enter_livi1' and arrivals_livi1 != None and arrivals_livi1 <= 3:
				vehicle_number = vehicles_livi1
			elif request.form.get('YES') == 'enter_livi2' and arrivals_livi2 != None and arrivals_livi2 <= 3:
				vehicle_number = vehicles_livi2
			elif request.form.get('YES') == 'enter_livi3' and arrivals_livi3 != None and arrivals_livi3 <= 3:
				vehicle_number = vehicles_livi3
			elif request.form.get('YES') == 'enter_LSC1' and arrivals_LSC1 != None and arrivals_LSC1 <= 3:
				vehicle_number = vehicles_LSC1
			elif request.form.get('YES') == 'enter_LSC2' and arrivals_LSC2 != None and arrivals_LSC2 <= 3:
				vehicle_number = vehicles_LSC2
			elif request.form.get('YES') == 'enter_LSC3' and arrivals_LSC3 != None and arrivals_LSC3 <= 3:
				vehicle_number = vehicles_LSC3
			elif request.form.get('YES') == 'enter_BSC1' and arrivals_BSC1 != None and arrivals_BSC1 <= 3:
				vehicle_number = vehicles_BSC1
			elif request.form.get('YES') == 'enter_BSC2' and arrivals_BSC2 != None and arrivals_BSC2 <= 3:
				vehicle_number = vehicles_BSC2
			elif request.form.get('YES') == 'enter_BSC3' and arrivals_BSC3 != None and arrivals_BSC3 <= 3:
				vehicle_number = vehicles_BSC3
			elif request.form.get('YES') == 'enter_arc1' and arrivals_allison1 != None and arrivals_allison1 <= 3:
				vehicle_number = vehicles_allison1
			elif request.form.get('YES') == 'enter_arc2' and arrivals_allison2 != None and arrivals_allison2 <= 3:
				vehicle_number = vehicles_allison2
			elif request.form.get('YES') == 'enter_arc3' and arrivals_allison3 != None and arrivals_allison3 <= 3:
				vehicle_number = vehicles_allison3
			elif request.form.get('YES') == 'enter_hill1' and arrivals_hill1 != None and arrivals_hill1 <= 3:
				vehicle_number = vehicles_hill1
			elif request.form.get('YES') == 'enter_hill2' and arrivals_hill2 != None and arrivals_hill2 <= 3:
				vehicle_number = vehicles_hill2
			elif request.form.get('YES') == 'enter_hill3' and arrivals_hill3 != None and arrivals_hill3 <= 3:
				vehicle_number = vehicles_hill3
			else:
				return redirect(url_for('weekendTwoBus'))

			session['current_bus'] = vehicle_number
			session['current_time'] = datetime.now().strftime("%H:%M:%S")
			session['current_route'] = 'Route Weekend-2'

			return redirect(url_for('exit_bus'))

	return render_template("WeekendTwoBus.html",
						   arrivals_CAstudentctr1=arrivals_CAstudentctr1,
						   arrivals_CAstudentctr2=arrivals_CAstudentctr2,
						   arrivals_CAstudentctr3=arrivals_CAstudentctr3,

						   arrivals_yard1=arrivals_yard1,
						   arrivals_yard2=arrivals_yard2,
						   arrivals_yard3=arrivals_yard3,

						   arrivals_SoCam1=arrivals_SoCam1,
						   arrivals_SoCam2=arrivals_SoCam2,
						   arrivals_SoCam3=arrivals_SoCam3,

						   arrivals_redOak1=arrivals_redOak1,
						   arrivals_redOak2=arrivals_redOak2,
						   arrivals_redOak3=arrivals_redOak3,

						   arrivals_lipman1=arrivals_lipman1,
						   arrivals_lipman2=arrivals_lipman2,
						   arrivals_lipman3=arrivals_lipman3,

						   arrivals_biel1=arrivals_biel1,
						   arrivals_biel2=arrivals_biel2,
						   arrivals_biel3=arrivals_biel3,

						   arrivals_henderson1=arrivals_henderson1,
						   arrivals_henderson2=arrivals_henderson2,
						   arrivals_henderson3=arrivals_henderson3,

						   arrivals_gibbons1=arrivals_gibbons1,
						   arrivals_gibbons2=arrivals_gibbons2,
						   arrivals_gibbons3=arrivals_gibbons3,

						   arrivals_collgehall1=arrivals_collgehall1,
						   arrivals_collegehall2=arrivals_collegehall2,
						   arrivals_collegehall3=arrivals_collegehall3,

						   arrivals_SACN1=arrivals_SACN1,
						   arrivals_SACN2=arrivals_SACN2,
						   arrivals_SACN3=arrivals_SACN3,

						   arrivals_livi1=arrivals_livi1,
						   arrivals_livi2=arrivals_livi2,
						   arrivals_livi3=arrivals_livi3,

						   arrivals_LSC1=arrivals_LSC1,
						   arrivals_LSC2=arrivals_LSC2,
						   arrivals_LSC3=arrivals_LSC3,

						   arrivals_BSC1=arrivals_BSC1,
						   arrivals_BSC2=arrivals_BSC2,
						   arrivals_BSC3=arrivals_BSC3,

						   arrivals_allison1=arrivals_allison1,
						   arrivals_allison2=arrivals_allison2,
						   arrivals_allison3=arrivals_allison3,

						   arrivals_hill1=arrivals_hill1,
						   arrivals_hill2=arrivals_hill2,
						   arrivals_hill3=arrivals_hill3,

						   capacity=capacity
						   )

@app.route("/Login", methods=['GET', 'POST'])
def login():
	session.pop('user_id', None)
	session.pop('user_stat', None)

	if request.method == 'POST':
		#session.pop('user_id', None)
		user = request.form['NET_ID']
		password = request.form['psw']

		c.execute("SELECT netID, password FROM USERS WHERE netID = ?", (user,))
		result = c.fetchone()

		if result:
			session['user_id'] = user
			pass_hash = c.execute("SELECT password, password FROM USERS WHERE netID = ?", (user,)).fetchone()[0]
			check_hash = bcrypt.check_password_hash(pass_hash, password)

			if check_hash == True:
				user_stat = c.execute("SELECT student_admin FROM USERS WHERE netID = ?", (user,)).fetchone()[0]
				session['user_stat'] = user_stat
				if user_stat == 'student':
					return redirect(url_for('home'))
				else:
					return redirect(url_for('admin_homepage'))
		else:
			#flash(f'Wrong Net ID or Password')
			return render_template("loginPage.html")

	#return redirect(url_for('home'))
	return render_template("loginPage.html")

@app.route("/SignUp", methods=['GET', 'POST'])
def signup():
	session.pop('user_id', None)
	session.pop('user_stat', None)

	if request.method == "POST":
		netid = request.form.get("NET_ID")
		phone = request.form.get("phone_no")
		pswd1 = request.form.get("psw")
		pswd2 = request.form.get("psw-repeat")
		usr_type = request.form.get("identity")
		grad = request.form.get("grad")

		#check if netid already exists
		c.execute("SELECT netID, password FROM USERS WHERE netID = ?", (netid,))
		result = c.fetchone()

		if result:
			return redirect(url_for('signup'))

		if pswd1 == pswd2:
			num = c.execute("SELECT count(*) from USERS").fetchone()
			index = num[0] + 1

			pass_hash = bcrypt.generate_password_hash(pswd1).decode('utf-8')
			c.execute("INSERT INTO USERS VALUES (:ID, :netID, :password, :phone_num, :student_admin, :graduation, :vehicle, :bus_name, :date, :time_on, :time_off, :COVID)",
					  {'ID': index,
					   'netID': netid,
					   'password': pass_hash,
					   'phone_num':phone,
					   'student_admin': usr_type,
					   'graduation': grad,
					   'vehicle': None,
					   'bus_name': None,
					   'date': None,
					   'time_on': None,
					   'time_off': None,
					   'COVID': 0})
			#c.execute("UPDATE USERS set vehicle=NULL, bus_name=NULL, time_on=NULL, time_off=NULL where netID = ?", (netid,))
			conn.commit()

		else:
			return redirect(url_for('signup'))

		if usr_type == 'student':
			return redirect(url_for('login'))
		elif usr_type == 'administrator':
			return redirect(url_for('admin_homepage'))

	return render_template("SignUpPage.html")

@app.route("/ExitBus", methods=['POST', 'GET'])
def exit_bus():
	if 'current_bus' not in session:
		return redirect(url_for('home'))
	else:
		current_user = session['user_id']
		if request.method == 'POST':
			if request.form.get('exit') == "undo":
				return redirect(url_for('home'))
			else:
				result = c.execute("SELECT vehicle, bus_name, time_on, time_off, date FROM USERS WHERE netID = ?", (current_user,)).fetchone()

				if result[0] == None or result[0] == '':
					c.execute("UPDATE USERS SET vehicle = ?, bus_name = ?, date = ?, time_on = ?, time_off = ? WHERE netID = ?", (session['current_bus'], session['current_route'], datetime.now().strftime("%Y-%m-%d"), session['current_time'], datetime.now().strftime("%H:%M:%S"), current_user))
					conn.commit()
					return redirect(url_for('home'))
				else:
					vehicle = result[0] + "," + session['current_bus']
					bus_name = result[1] + "," + session['current_route']
					time_on = result[2] + "," + session['current_time']
					exit_time = result[3] + "," + datetime.now().strftime("%H:%M:%S")
					date = result[4] + "," + datetime.now().strftime("%Y-%m-%d")

					c.execute("UPDATE USERS SET vehicle = ?, bus_name = ?, date = ?, time_on = ?, time_off = ? WHERE netID = ?", (vehicle, bus_name, date, time_on, exit_time, current_user))
					conn.commit()
					return redirect(url_for('home'))

	return render_template("ExitBusPage.html")

@app.route("/AdminHomepage", methods=['POST', 'GET'])
def admin_homepage():
	session.pop('netid', None)

	if 'user_id' not in session:
		return redirect(url_for('login'))
	else:
		if request.method == 'POST':
			student_name = request.form.get('NET_ID')
			#check if netid in database
			c.execute("SELECT netID FROM USERS WHERE netID = ?", (student_name,))
			result = c.fetchone()

			if result:
				session['netid'] = student_name
				return redirect(url_for('studentRecord'))
			else:
				return redirect(url_for('admin_homepage'))

	return render_template("adminHomepage.html")


@app.route("/studentRecord")
def studentRecord():
	if 'netid' not in session:
		return redirect(url_for('admin_homepage'))
	else:
		student = session['netid']

		result = c.execute("SELECT phone_num, graduation, COVID FROM USERS WHERE netID = ?", (student,)).fetchone()
		phone = result[0]
		grad = result[1]
		covid = result[2]

		if covid == 1:
			covid = 'POSITIVE'
		else:
			covid = 'NEGATIVE'

		result = c.execute("SELECT vehicle, time_on, date FROM USERS where netID = ?", (student,)).fetchone()
		vehicle = result[0]
		time_on = result[1]
		date = result[2]

		if vehicle == None and time_on == None:
			ride_info = {}
			contact_info = {}
		else:
			ride_info = student_rec(vehicle, time_on, date)
			contact_dict, student_list = contact_tracing(student)
			contact_info = contact_rec(contact_dict, student_list)
	return render_template("studentRecord.html", covid=covid, student=student, phone=phone, grad=grad, ride_info=ride_info, contact_info=contact_info)

if __name__ == "__main__":
	#app.run(host='172.31.131.201', debug=True)
	app.run(debug=True)
