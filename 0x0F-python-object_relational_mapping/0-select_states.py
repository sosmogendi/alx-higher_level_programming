#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all three arguments (username, password, database name) are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name,
            charset="utf8"
        )

        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Execute the SELECT query
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch and print the results
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Close the cursor and the database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)
