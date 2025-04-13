import sqlite3
import pandas as pd

def query_db(query):
    print('hi')
    conn = sqlite3.connect(r"db/rossman_db.sqlite")
    cursor = conn.cursor()

    # Execute the SQL query to get the list of tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Fetch all the results
    tables = cursor.fetchall()

    # Print the list of tables
    if tables:
        print("Tables in the database:")
        for table in tables:
            print(table[0])  # The table name is the first element of the tuple
    else:
        print("No tables found in the database.")
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df