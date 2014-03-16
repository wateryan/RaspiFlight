#!/usr/bin/python
###############################
#                             #
#   RaspiFlight GPS Module    #
#            v0.25            #
#                             #
# Parses GPS output from      # 
# ttyAMA0 serial connection   #
# on the Raspberry Pi         #
#                             #
###############################

import csv
import os
import serial
import re

class GPS:
        # For serial connection
        addr = 0
        baud = 0
        # GPS Position Info
        time = 0
        date = 0
        status = 'V'
        latitude = [] 
        longtitude = []
        groundSpeed = 0
        trackAngle = 0
        magneticVariation = []
        checksum = '0'
        def __init__(self):
                self.addr = '/dev/ttyAMA0'
                self.baud = 9600
                print "GPS Initialized"

        def update_GPS(self):
                ser = serial.Serial(self.addr, self.baud)
                x = ''
                while not x.startswith('$GPRMC'):
                        x = ser.readline()
                        
                x = x.split(",")
                self.time = x[1]
                self.status = x[2]
                self.latitude.extend((x[3],x[4]))
                self.longtitude.extend((x[5], x[6]))
                self.groundSpeed = x[7]
                self.trackAngle = x[8]
                self.date = x[9]
                self.magneticVariation.extend((x[10],x[11]))
                self.checksum = x[12]                 

        def getTime(self):
                currtime = re.findall(r'.{1,2}',self.time)
                hour = currtime[0]
                minute = currtime[1]
                second = currtime[2]
                
                return "%s:%s:%s" % (hour,minute,second,) 

        def getDate(self):
                currdate = re.findall(r'.{1,2}',self.date)
                day = currdate[0]
                month = currdate[1]
                year = currdate[2]

                return "%s/%s/%s" % (day,month,year,)

        def getStatus(self):
                return "%s" % (self.status)

        #LONG AND LAT are untested due to problems getting a fix in the dorms
        def getLatitude(self):
                #Check if Active
                if self.status == 'A':
                        lat = self.latitude[0][:2]
                        deg = self.latitude[0][2:]
                        NS = self.latitude[1]
                        return "Lat %s deg %s' %s" % (lat, deg, NS,)
                else:
                        return "N/A"

        def getLongtitude(self):
                if self.status == 'A':
                        lon = self.longtitude[0][:2]
                        deg = self.longtitude[0][2:]
                        EW = self.longtitude[1]
                        return "Long %s deg %s' %s" % (lon,deg,EW,)
                else:
                        return "N/A"

        def getSpeed(self):
                return "%s knots" % (self.groundSpeed,)

        def getTrackAngle(self):
                return "%s Degrees True" % (self.trackAngle,)

        def getMagneticVariation(self):
                if self.status == 'A':
                        return "%s,%s" % (self.magneticVariation[0],self.magneticVariation[1],)
                else:
                        return "N/A"
        def getChecksum(self):
                return "%s" % (self.checksum,)

GPS = GPS()
