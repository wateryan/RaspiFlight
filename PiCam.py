#!/usr/bin/env python
###############################
#                             #
# RaspiFlight Camera Module   #
#            v0.02            #
#                             #
# Parses the user config file #
# and executes the raspi cam  #
# command                     #
#                             #
###############################

#Imports
import os
import sys
import subprocess

class PiCam:
	CONFIG_FILE = "piCamConfig.conf"
	camConfig = []
	stillConfig = []
	vidConfig = []

	def __init__(self):
		if self.readConfig():
                        print "Camera Initialized"
                else:
                        print >> sys.stderr, "Camera NOT Initialized"

	def readConfig(self):
		if os.path.isfile(self.CONFIG_FILE):
			with open(self.CONFIG_FILE) as f:
				for line in f:
					if line.startswith(('c')):
						self.camConfig.append([])
						(property, ext, val) = line.split()
						self.camConfig[len(self.camConfig)-1].append(property)
						self.camConfig[len(self.camConfig)-1].append(ext)
						self.camConfig[len(self.camConfig)-1].append(val)
					elif line.startswith(('i')):
						self.stillConfig.append([])
						(property, ext, val) = line.split()
						self.stillConfig[len(self.stillConfig)-1].append(property)
						self.stillConfig[len(self.stillConfig)-1].append(ext)
						self.stillConfig[len(self.stillConfig)-1].append(val)
					elif line.startswith(('v')):
						self.vidConfig.append([])
						(property, ext, val) = line.split()
						self.vidConfig[len(self.vidConfig)-1].append(property)
						self.vidConfig[len(self.vidConfig)-1].append(ext)
						self.vidConfig[len(self.vidConfig)-1].append(val)
                        return True
		else:
			print >> sys.stderr, 'Unable to locate Configuration file'
			return False

	def executePhoto(self):
		cmd = ["raspistill"]
		for i in range(0, len(self.camConfig)):
			if self.camConfig[i][2].lower() != "false" and self.camConfig[i][2].lower() != "true":
				cmd.append(self.camConfig[i][1])
				cmd.append(self.camConfig[i][2])
			elif self.camConfig[i][2].lower() == "true":
				cmd.append(self.camConfig[i][1])
		for i in range(0, len(self.stillConfig)):
			if self.stillConfig[i][2].lower() != "false" and self.stillConfig[i][2].lower() != "true":
				cmd.append(self.stillConfig[i][1])
				cmd.append(self.stillConfig[i][2])
			elif self.stillConfig[i][2].lower() == "true":
				cmd.append(self.stillConfig[i][1])
		subprocess.call(cmd)

	def executeVid(self):
		cmd = ["raspivid"]
		for i in range(0, len(self.camConfig)):
			if self.camConfig[i][2].lower() != "false" and self.camConfig[i][2].lower() != "true":
				cmd.append(self.camConfig[i][1])
				cmd.append(self.camConfig[i][2])
			elif camConfig[i][2].lower() == "true":
				cmd.append(self.camConfig[i][1])
		for i in range(0, len(self.idConfig)):
			if self.vidConfig[i][2].lower() != "false" and self.vidConfig[i][2].lower() != "true":
				cmd.append(self.vidConfig[i][1])
				cmd.append(self.vidConfig[i][2])
			elif self.vidConfig[i][2].lower() == "true":
				cmd.append(self.vidConfig[i][1])
		subprocess.call(cmd)

PiCam = PiCam()
