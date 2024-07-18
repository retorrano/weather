import sqlite3
import os

def check_or_create_settings_db():
    # Check if settings.db file exists
    if os.path.isfile('settings.db'):
        # Connect to the database
        conn = sqlite3.connect('settings.db')
        cursor = conn.cursor()

        # Check if the 'main' table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='main'")
        table_exists = cursor.fetchone()

        if table_exists:
            # Check if the required fields exist in the 'main' table
            cursor.execute("PRAGMA table_info(main)")
            columns = cursor.fetchall()
            required_fields = ['latitude', 'longitude', 'api']
            fields_exist = all(field in [column[1] for column in columns] for field in required_fields)

            if fields_exist:
                print("The settings.db file exists and contains the correct 'main' table with the required fields.")
            else:
                print("The settings.db file exists but the 'main' table is missing the required fields.")
        else:
            print("The settings.db file exists but the 'main' table is missing.")
    else:
        # Create the settings.db file and the 'main' table with the required fields
        conn = sqlite3.connect('settings.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE main (latitude REAL, longitude REAL, api TEXT)")
        print("The settings.db file and the 'main' table have been created.")

    conn.close()
