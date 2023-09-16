#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        sys.exit(1)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SELECT query
    try:
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()
    except MySQLdb.Error as e:
        print("Error executing query:", e)
        sys.exit(1)

    # Use a set to keep track of unique states
    unique_states = set()

    # Display the results without duplicates
    for state in states:
        if state[1] not in unique_states:
            print(state)
            unique_states.add(state[1])

    # Close the cursor and database connection
    cursor.close()
    db.close()
