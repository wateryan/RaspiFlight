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
		readConfig()

	def readConfig():
		if os.path.isfile(CONFIG_FILE):
			with open(CONFIG_FILE) as f:
				for line in f:
					if line.startswith(('c')):
						camConfig.append([])
						(property, ext, val) = line.split()
						camConfig[len(camConfig)-1].append(property)
						camConfig[len(camConfig)-1].append(ext)
						camConfig[len(camConfig)-1].append(val)
					elif line.startswith(('i')):
						stillConfig.append([])
						(property, ext, val) = line.split()
						stillConfig[len(stillConfig)-1].append(property)
						stillConfig[len(stillConfig)-1].append(ext)
						stillConfig[len(stillConfig)-1].append(val)
					elif line.startswith(('v')):
						vidConfig.append([])
						(property, ext, val) = line.split()
						vidConfig[len(vidConfig)-1].append(property)
						vidConfig[len(vidConfig)-1].append(ext)
						vidConfig[len(vidConfig)-1].append(val)
		else:
			print >> sys.stderr, 'Unable to locate Configuration file'
			
	def executePhoto():
		cmd = ["raspistill"]
		for i in range(0, len(camConfig)):
			if camConfig[i][2].lower() != "false" and camConfig[i][2].lower() != "true":
				cmd.append(camConfig[i][1])
				cmd.append(camConfig[i][2])
			elif camConfig[i][2].lower() == "true":
				cmd.append(camConfig[i][1])
		for i in range(0, len(stillConfig)):
			if stillConfig[i][2].lower() != "false" and stillConfig[i][2].lower() != "true":
				cmd.append(stillConfig[i][1])
				cmd.append(stillConfig[i][2])
			elif stillConfig[i][2].lower() == "true":
				cmd.append(stillConfig[i][1])
		subprocess.call(cmd)

	def executeVid():
		cmd = ["raspivid"]
		for i in range(0, len(camConfig)):
			if camConfig[i][2].lower() != "false" and camConfig[i][2].lower() != "true":
				cmd.append(camConfig[i][1])
				cmd.append(camConfig[i][2])
			elif camConfig[i][2].lower() == "true":
				cmd.append(camConfig[i][1])
		for i in range(0, len(vidConfig)):
			if vidConfig[i][2].lower() != "false" and vidConfig[i][2].lower() != "true":
				cmd.append(vidConfig[i][1])
				cmd.append(vidConfig[i][2])
			elif vidConfig[i][2].lower() == "true":
				cmd.append(vidConfig[i][1])
		subprocess.call(cmd)