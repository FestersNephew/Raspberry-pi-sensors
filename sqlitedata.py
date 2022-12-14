import sqlite3

# Connect to the database
conn = sqlite3.connect('sensor_data.db')

# Create a cursor
cursor = conn.cursor()

# Create a table to store the sensor data
cursor.execute('''
    CREATE TABLE sensor_data (
        timestamp TEXT,
        temperature REAL,
        humidity REAL
    )
''')

# Function to insert data into the database
def insert_data(timestamp, temperature, humidity):
    cursor.execute('''
        INSERT INTO sensor_data (timestamp, temperature, humidity)
        VALUES (?, ?, ?)
    ''', (timestamp, temperature, humidity))
    conn.commit()

# Example data
insert_data('2022-12-14 12:00:00', 72.5, 37.5)

# Close the database connection
conn.close()
