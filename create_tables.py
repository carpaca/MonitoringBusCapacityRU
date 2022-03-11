import sqlite3

conn = sqlite3.connect('capstone.db')
c = conn.cursor()

"""create database tables"""

#c.execute("DROP TABLE TEST_TABLE")
#c.execute("DROP TABLE STOPS")
#c.execute("DROP TABLE USERS")
#c.execute("DROP TABLE TEST_ROUTES")
#c.execute("DROP TABLE BUSSES")

c.execute("""CREATE TABLE STOPS(
            ID integer,
            stopID integer,
            stopName text,
            PRIMARY KEY(ID)
            )""")

c.execute("""CREATE TABLE ROUTES(
            ID integer,
            routeID integer,
            routeName integer,
            PRIMARY KEY(ID)
            )""")

c.execute("""CREATE TABLE VEHICLES(
            ID integer,
            vehicleID integer,
            capacity integer,
            routeID integer,
            PRIMARY KEY(ID)
            )""")

#c.execute("""CREATE TABLE BUSSES(
#            ID integer,
#            vehicle_number integer,
#            capacity integer,
#            route integer,
#            stops integer,
#            arrival text,
#            lat text,
#            long_text,
#            PRIMARY KEY(ID)
#            )""")

#0 for admin, 1 for student
c.execute("""CREATE TABLE USERS(
            ID integer,
            netID text,
            password text,
            phone_num text,
            student_admin int,
            vehicle text,
            bus_name text,
            COVID integer,
            PRIMARY KEY(ID)
            )""")

#c.execute("INSERT OR REPLACE INTO USERS VALUES (:ID, :netID, :password, :student_admin, :VEHICLE_TODAY, :BUSSES_TODAY, :COVID)",
#          {'ID': 2,
#           'netID': 'abc123',
#           'password': 'asdfjkl',
#           'student_admin': 0,
#           'VEHICLE_TODAY': 'NONE',
#           'BUSSES_TODAY': 'NONE',
#           'COVID': 0})

conn.commit()
conn.close()
