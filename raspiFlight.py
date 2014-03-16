#!/usr/bin/python
#
###############################
#                             #
#        RaspiFlight          #
#          v0.01              #
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
from BMP import BMP
from PiCam import PiCam

pictureInterval=5

def checkPrivelages():
        # Check root priv
        # Required to use Barometer
        if not os.geteuid()==0:
                print "\nRoot privelages required to run.\n"
                sys.exit(1)     

def interface():
        subprocess.call(["clear"])
        print "|---------------------------------"
        print "| Current Temperature : %.2f" % (BMP.getTemp())
        print "| Current Pressure    : %.2f" % (BMP.getPressure()/100)
        print "| Current Altitude    : %.2f" % (BMP.getAltitude())
        print "|---------------------------------"
        threading.Timer(2, interface).start()

def takePhoto():
        print "TAKE A PHOTO"
        # PiCam.executePhoto()
        threading.Timer(pictureInterval, takePhoto).start()
def run():
        interface_thread = threading.Thread(target=interface)
        interface_thread.daemon = True
        interface_thread.start()
        
        photo_thread = threading.Thread(target=takePhoto)
        photo_thread.daemon = True
        photo_thread.start()
        try:
                while True:
                        interface_thread.join(1)
                        photo_thread.join(1)
        except KeyboardInterrupt:
                print "^C Caught. Exit."
                


checkPrivelages()
run()
