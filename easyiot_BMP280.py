#!/usr/bin/env python

import time
from bmp280 import BMP280
import requests

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

# Initialise the BMP280
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

temperature = bmp280.get_temperature()
pressure = bmp280.get_pressure()
temperature = bmp280.get_temperature()
pressure = bmp280.get_pressure()
#print('{:04.1f}*C {:04.0f}hPa'.format(temperature, pressure))

url="http://192.168.1.214/Api/EasyIoT/Control/Module/Virtual/N2S0/ControlLevel/"+str(round(temperature,1))
#print(url)

r = requests.get(url, auth=('sensor', 'sensor'))
#print(r.status_code)

url="http://192.168.1.214/Api/EasyIoT/Control/Module/Virtual/N6S0/ControlLevel/"+str(round(pressure,1))
#print(url)

r = requests.get(url, auth=('sensor', 'sensor'))
#print(r.status_code)
