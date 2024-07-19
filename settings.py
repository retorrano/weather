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
            required_fields = ['latitude', 'longitude', 'api', 'refresh_rate']
            existing_fields = [column[1] for column in columns]
            fields_exist = all(field in existing_fields for field in required_fields)

            if fields_exist:
                print("The settings.db file exists and contains the correct 'main' table with the required fields.")
            else:
                print("The settings.db file exists but the 'main' table is missing some required fields.")
                if 'refresh_rate' not in existing_fields:
                    cursor.execute("ALTER TABLE main ADD COLUMN refresh_rate INTEGER")
                    print("Added 'refresh_rate' field to the 'main' table.")
        else:
            print("The settings.db file exists but the 'main' table is missing.")
            # Create the 'main' table with the required fields
            cursor.execute("CREATE TABLE main (latitude REAL, longitude REAL, api TEXT, refresh_rate INTEGER)")
            print("Created 'main' table with required fields.")
    else:
        # Create the settings.db file and the 'main' table with the required fields
        conn = sqlite3.connect('settings.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE main (latitude REAL, longitude REAL, api TEXT, refresh_rate INTEGER)")
        print("The settings.db file and the 'main' table have been created.")

    conn.close()

def get_settings():
    conn = sqlite3.connect('settings.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT latitude, longitude, api, refresh_rate FROM main LIMIT 1")
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return {'latitude': result[0], 'longitude': result[1], 'api': result[2], 'refresh_rate': result[3]}
    else:
        return {'latitude': '', 'longitude': '', 'api': '', 'refresh_rate': ''}
