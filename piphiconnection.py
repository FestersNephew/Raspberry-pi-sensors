import requests

# Replace these values with the details of your sensor and PiPHi network
sensor_name = "my_sensor"
sensor_type = "temperature"
sensor_units = "celsius"
piphi_url = "http://pi.phi/api"

# Register the sensor with the PiPHi network
url = f"{piphi_url}/register"
data = {
    "name": sensor_name,
    "type": sensor_type,
    "units": sensor_units
}
response = requests.post(url, json=data)

if response.status_code == 200:
    print(f"Successfully registered {sensor_name} on the PiPHi network")
else:
    print(f"Failed to register {sensor_name} on the PiPHi network")
