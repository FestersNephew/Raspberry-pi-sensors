# Import the necessary libraries
import Adafruit_DHT
import time

# Set the type of sensor that you are using (in this case, a DHT22)
sensor = Adafruit_DHT.DHT22

# Set the GPIO pin that the DHT22 is connected to
pin = 4

# Main loop to read the sensor data and display it
while True:
    # Read the humidity and temperature from the sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    # If the readings are valid, display them
    if humidity is not None and temperature is not None:
        print("Temperature: {0:0.1f} C    Humidity: {1:0.1f} %".format(temperature, humidity))
    else:
        print("Failed to retrieve data from the sensor")
    
    # Wait a few seconds before reading the sensor again
    time.sleep(2)
