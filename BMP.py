#!/usr/bin/python
###############################
#                             #
#        RaspiFlight          #
#          v0.01              #
#                             #
# Module for Barometric, Temp #
# and altitude sensors        #
#                             #
###############################

# Import Adafruit I2C for the the Sensor
from Adafruit_Library.Adafruit_BMP085 import BMP085

class BMP:
        bmp = None
        temp = 0
        pressure = 0
        altitude = 0

        def __init__(self):
                if self.bmp == None:
                        self.bmp = BMP085(0x77)
                        print "Initialized Barometric Sensor"

        def getTemp(self):
                return self.bmp.readTemperature()

        def getPressure(self):
                return self.bmp.readPressure()

        def getAltitude(self):
                return self.bmp.readAltitude((self.bmp.readPressure() * 100))

BMP = BMP()
