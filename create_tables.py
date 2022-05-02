import sqlite3

conn = sqlite3.connect('capstone.db')
c = conn.cursor()

"""create database tables"""

#c.execute("DROP TABLE TEST_TABLE")
#c.execute("DROP TABLE VEHICLES")
c.execute("DROP TABLE USERS")
#c.execute("DROP TABLE ROUTES")
#c.execute("DROP TABLE TEST_ROUTES")
#c.execute("DROP TABLE BUSSES")

#c.execute("""CREATE TABLE STOPS(
#            ID integer,
#            stopID integer,
#            stopName text,
#            PRIMARY KEY(ID)
#            )""")

#c.execute("""CREATE TABLE ROUTES(
#            ID integer,
#            routeID integer,
#            routeName integer,
#            PRIMARY KEY(ID)
#            )""")

#c.execute("""CREATE TABLE VEHICLES(
#            ID integer,
#            vehicleID integer,
#            capacity integer,
#            routeID integer,
#            PRIMARY KEY(ID)
#            )""")

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
            student_admin integer,
            graduation integer,
            vehicle text,
            bus_name text,
            date text,
            time_on text,
            time_off text,
            COVID integer,
            PRIMARY KEY(ID)
           )""")

#c.execute("INSERT OR REPLACE INTO USERS VALUES (:ID, :netID, :password, :phone_num, :student_admin, :vehicle, :bus_name, :COVID)",
#          {'ID': 2,
#           'netID': 'cde456',
#           'password': 'asdfjkl',
#           'phone_num':999-999-9999,
#           'student_admin': 0,
#           'vehicle': 'none',
#           'bus_name': 'something',
#           'COVID': 0})

# get number of already existing users in table
#num = c.execute("SELECT count(*) from USERS").fetchone()

#get next ID number for next user to input
#print(num[0]+1)

#out = c.execute("SELECT netID FROM USERS WHERE netID = ?", ('csj40',)).fetchone()[0]
#print(out)

#result = c.execute("SELECT time_on FROM USERS WHERE ID = ?", (1,)).fetchone()

#array = result[0]
#array = array.split(",")[1:len(array)]
#array = [1,2,3,4,5]
#print(array)
conn.commit()
conn.close()
