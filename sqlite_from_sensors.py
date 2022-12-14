import sqlite3
import Adafruit_DHT
import smbus
import time

# I2C bus
bus = smbus.SMBus(1)

# Connect to the database
conn = sqlite3.connect('sensor_data.db')

# Create a cursor
cursor = conn.cursor()

# Create a table to store the sensor data
cursor.execute('''
    CREATE TABLE sensor_data (
        timestamp TEXT,
        temperature REAL,
        humidity REAL,
        light INTEGER,
        moisture INTEGER
    )
''')

# Function to insert data into the database
def insert_data(timestamp, temperature, humidity, light, moisture):
    cursor.execute('''
        INSERT INTO sensor_data (timestamp, temperature, humidity, light, moisture)
        VALUES (?, ?, ?, ?, ?)
    ''', (timestamp, temperature, humidity, light, moisture))
    conn.commit()

# Read data from the DHT22 sensor
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 17)

# Read data from the GY30 sensor
light = bus.read_byte_data(0x23, 0x11)

# Read data from the YL69 sensor
moisture = bus.read_byte_data(0x20, 0x04)

# Insert the data into the database
insert_data(time.strftime('%Y-%m-%d %H:%M:%S'), temperature, humidity, light, moisture)

# Close the database connection
conn.close()
