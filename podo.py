# -*- coding: utf-8 -*- 

import threading
import subprocess
import os
import sys
import glob

def banner():
	os.system("clear")
	print "                O=(‘-‘Q)   "               
	print "        .--.  .--. .--.  .--.       .--. .   ..   . .--..   ."
	print "        |   ):    :|   ::    :      |   )|   ||\  |:    |   |"
	print "        |--' |    ||   ||    | ____ |--' |   || \ ||    |---|"
	print "        |    :    ;|   ;:    ;      |    :   ;|  \|:    |   |"
	print "        '     `--' '--'  `--'       '     `-' '   ' `--''   '"

	print data
	print "\n------------------------- Usage -----------------------------"
	print "1 -> Install all apk on all devices"
	print "2 -> Capture log all devices"
	print "3 -> List of Devices"
	print "x -> Exit this program"
	print "-------------------------------------------------------------"

appList = glob.glob("./*.apk")
appListCount = len(appList)
cmd = ['adb','devices']
fd_popen = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True).stdout
data = fd_popen.read().strip()
fd_popen.close()
data = data.split('\n')
del(data[0])

def listOfDevices():
	print "List of Devices"
	for i in range(len(data)):
		tmp = data[i].find('\t')
		data[i] = data[i][:tmp]
		print "["+str(i+1)+"] "+data[i]+"\n"
	raw_input("Press any key.\n")

def runThread(query):
	for i in range(appListCount):
		print query+appList[i]
		#os.system(query+appList[i])

def installAllDevices():
	threads = []
	cbe = "adb -s "
	caf = " install "
	query =[]
	for i in range(len(data)):
		tmp = data[i].find('\t')
		data[i] = data[i][:tmp]
		query.append(cbe+data[i]+caf)
		q=cbe+data[i]+caf
		t = threading.Thread(target=runThread,args=(q,))
		t.start()	
	for t in threads:
		t.join()
	raw_input("Press any key.\n")

#adb shell screencap -p /sdcard/sc.png
#adb pull /sdcard/sc.png	

os.system("adb devices")
while(1):
	banner()
	cmd = raw_input("CMD>: ")
	if(cmd == "x"):
		exit()
	elif(cmd == "1"):
		installAllDevices()
	elif(cmd == "2"):
		pass
	elif(cmd == "3"):
		listOfDevices()	
		result = 0
	



