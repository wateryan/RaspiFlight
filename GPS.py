#!/usr/bin/python

import csv

class GPS:
        nmea_line = None
        def __init__(self):
                for line in csv.reader(open('/dev/ttyAMAO')):
                        print line

gps = GPS()

