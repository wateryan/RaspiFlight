===============
  RaspiFlight
===============

Part of a flight controller module for the RaspberryPi. Manages a GPS module, Barometric/Altitude/Temperature sensors, and a camera module.

---------------
  pre Launch
---------------

Last minute change on the pi hardware itself that made
RaspiFlight redirect output to a file instead of stdout.
This isn't reflected in the code here because this change
was made in the field. We were still having too many errors
with radio transmission to risk losing ALL of the data
that could have been collected.

The only thing that would have been different is that
I (ryan) changed all the ui "print" statements to out.write()
which appended to a file in the local directory. The rest of the code
is as it was the day of the launch.


---------------
     v0.30
---------------
-RaspiFlight.py
  -Added GPS to UI

-GPS.py
  -Removed test code

---------------
     v0.25
---------------
-RaspiFlight.py
  -Made as entry point to the program
  -Created interface to display program output

-piCam.py
  -Changed from a class to a script to enable usage by RaspiFlight.py
  -renamed to PiCam.py
  
-BMP.py
  -general bug fixes and some cleanup of the code

---------------
     v0.01
---------------
-Attached program to Adafruit library for use of the Sensors on the Barometer module

-RaspiFlight
        Added
        Will later make use of as the "main" point of entry into the program

-BMP.py
        Initializes the sensors on the Barometer and can make calls to get
        Temperature (In C), Altitude (approximate), and Pressure

-piCam.py
  -Added function to parse .conf file
  -Executes both Stills and Video

-PiCamConfig.py was removed. Not worth the effor to implement right now.
  Just configure the .conf manually. Instructions are inside of the file.
