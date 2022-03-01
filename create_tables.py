import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

"""create database tables"""

#c.execute("DROP TABLE TEST_TABLE")
#c.execute("DROP TABLE STOPS")
#c.execute("DROP TABLE STUDENTS")
#c.execute("DROP TABLE TEST_ROUTES")
#c.execute("DROP TABLE BUSSES")

c.execute("""CREATE TABLE STOPS(
            ID integer, 
            stopID integer,
            stopName text,
            routes integer,
            PRIMARY KEY(ID)
            )""")

c.execute("""CREATE TABLE TEST_ROUTES(
            ID integer,
            routeID integer,
            routeName integer,
            STOPS text,
            PRIMARY KEY(ID)
            )""")

c.execute("""CREATE TABLE TEST_TABLE(
            ID integer,
            vehicleID integer,
            capacity integer,
            routeNAME text,
            routeID integer,
            stopNAME text,
            nextSTOP integer,
            arrivals text,
            lat_long text,
            PRIMARY KEY(ID)
            )""")

c.execute("""CREATE TABLE BUSSES(
            ID integer,
            vehicle_number integer,
            capacity integer,
            route integer,
            stops integer,
            arrival text,
            lat text,
            long_text,
            PRIMARY KEY(ID)
            )""")

c.execute("""CREATE TABLE STUDENTS(
            ID integer,
            netID text,
            VEHICLE_TODAY integer,
            BUSSES_TODAY text,
            COVID integer,
            PRIMARY KEY(ID)
            )""")

conn.commit()
conn.close()
