#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        sys.exit(1)

    cursor = db.cursor()

    query = "SELECT cities.name FROM cities \
             INNER JOIN states ON states.id = cities.state_id \
             WHERE states.name = %s \
             ORDER BY cities.id ASC"

    try:
        cursor.execute(query, (state_name,))
        cities = cursor.fetchall()
    except MySQLdb.Error as e:
        print("Error executing query:", e)
        sys.exit(1)

    city_names = [city[0] for city in cities]
    result = ", ".join(city_names)
    print(result)

    cursor.close()
    db.close()
