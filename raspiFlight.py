#!/usr/bin/python
#
###############################
#                             #
#        RaspiFlight          #
#          v0.30              #
#                             #
# Main module for RespiFlight #
# Controls the Barometer,     #
# GPS, and Camera for the     #
# Raspberry Pi                #
#                             #
###############################

import os
import sys
import threading
import subprocess
# Import RaspiFlight
from PiCam import PiCam
from GPS import GPS

pictureInterval=5 # in seconds

def checkPrivelages():
        # Check root priv
        # Required to use Barometer
        if os.geteuid()!=0:
                print "\nBarometer requires root privelages required to run.\n"
                print "Exiting..."
                sys.exit(1)
        else:
                global BMP
                from BMP import BMP
                

def interface():
        GPS.update_GPS()
        subprocess.call(["clear"])
        print "|--------------------------------|"
        print "| Date: %-8s  Time: %-8s |" % (GPS.getDate(),GPS.getTime(),)
        print "| Current Temperature : %.2f    |" % (BMP.getTemp(),)
        print "| Current Pressure    : %.2f   |" % ((BMP.getPressure()/100),)
        print "| Current Altitude    : %.2f |" % (BMP.getAltitude(),)
        print "| GPS Status          : %s        |" % (GPS.getStatus(),)
        print "| Lat : %-24s |" % (GPS.getLatitude(),)
        print "| Long: %-24s |" % (GPS.getLongtitude(),)
        print "| Speed:%-24s |" % (GPS.getSpeed(),)
        print "| Angle:%-24s |" % (GPS.getTrackAngle(),)
        print "| Magnetic Variation: %-10s |" % (GPS.getMagneticVariation(),)
        print "|--------------------------------|"
        
        
        threading.Timer(2, interface).start()

def takePhoto():
        # For testing -- don't want to store all the test photos
        print "TAKE A PHOTO"
        # PiCam.executePhoto()
        threading.Timer(pictureInterval, takePhoto).start()
def run():
        # Runs the UI
        interface_thread = threading.Thread(target=interface)
        interface_thread.daemon = True
        interface_thread.start()

        # Takes photos in the background
        photo_thread = threading.Thread(target=takePhoto)
        photo_thread.daemon = True
        photo_thread.start()
        try:
                while True:
                        interface_thread.join(1)
                        photo_thread.join(1)
        except KeyboardInterrupt:
                print "^C Caught. Exit."
                os._exit(0)

checkPrivelages()
run()
