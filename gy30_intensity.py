#assumes HY30 sensor is set up to the 12C bus on the Pi
#first need to install smbus library with pip install smbus
# Import the necessary libraries
import smbus
import time

# Set the I2C address of the GY-30 sensor
address = 0x23

# Initialize the I2C bus
bus = smbus.SMBus(1)

# Main loop to read the sensor data and display it
while True:
    # Read the light intensity from the sensor
    light_intensity = bus.read_i2c_block_data(address, 0x10)[0]
    
    # Display the light intensity in an easy-to-read format
    print("Light intensity: {0:0.1f} lux".format(light_intensity))
    
    # Wait a few seconds before reading the sensor again
    time.sleep(2)
