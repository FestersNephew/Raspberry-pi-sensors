# Import the necessary libraries
import RPi.GPIO as GPIO
import time

# Set the GPIO pin that the HC-38 module is connected to
pin = 4

# Set the threshold for the moisture readings (below this value the soil is considered dry)
moisture_threshold = 400

# Initialize the GPIO library
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

# Main loop to read the sensor data and display it
while True:
    # Read the moisture level from the sensor
    moisture_level = GPIO.input(pin)
    
    # Determine if the soil is moist or dry based on the moisture threshold
    if moisture_level < moisture_threshold:
        print("Soil moisture: DRY")
    else:
        print("Soil moisture: MOIST")
    
    # Wait a few seconds before reading the sensor again
    time.sleep(2)
