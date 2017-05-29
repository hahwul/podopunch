# -*- coding: utf-8 -*- 

import threading
import subprocess
import os
import sys
import glob
from datetime import datetime

def banner():
	os.system("clear")
	print "\n                O=(‘-‘Q)   "               
	print "        .--.  .--. .--.  .--.       .--. .   ..   . .--..   ."
	print "        |   ):    :|   ::    :      |   )|   ||\  |:    |   |"
	print "        |--' |    ||   ||    | ____ |--' |   || \ ||    |---|"
	print "        |    :    ;|   ;:    ;      |    :   ;|  \|:    |   |"
	print "        '     `--' '--'  `--'       '     `-' '   ' `--''   '"
	print "   [Easy testing from multiple android devices] + [by hahwul]"

def usage():
	banner()
	print "\nChoice mode(Input number)"
	print "------------------------- CMD -----------------------------"
	print " [1] -> Install all APK(single or all devices)"
	print " [2] -> Capture log(single or all devices)"
	print " [3] -> List of Devices"
	print " [x] -> Exit this program"
	print "-------------------------------------------------------------"

def usage_1():
	banner()
	print "\n[1] Install all APK Mode"
	print "------------------------- CMD -----------------------------"
	print " [1] -> Single Device"
	print " [2] -> All Devices"
	print " [x] -> Come back Home"
	print "-------------------------------------------------------------"

def usage_choice():
	banner()
	print "\n[1-1] Choice device(Input number)"
	print "------------------------- CMD -----------------------------"

def usage_2():
	banner()
	print "\n[2] Capture log"
	print "------------------------- CMD -----------------------------"
	print " [1] -> Single Device"
	print " [2] -> All Devices"
	print " [x] -> Come back Home"
	print "-------------------------------------------------------------"

appList = glob.glob("./*.apk")
appListCount = len(appList)
fd_popen = subprocess.Popen("adb devices",stdout=subprocess.PIPE, shell=True).stdout
data = fd_popen.read().strip()
fd_popen.close()
data = data.split('\n')
del(data[0])

def listOfDevices():
	print "List of Devices"
	for i in range(len(data)):
		tmp = data[i].find('\t')
		data[i] = data[i][:tmp]
		print " + ["+str(i+1)+"]  -->  "+data[i]+"\n"
	raw_input("Press any key.\n")

def runThread(query,atype,threadNum):
	if(atype == "apk"):
		for i in range(appListCount):
			print "running.. "+query+appList[i]
			os.system(query+appList[i])
	elif(atype == "log"):
		print "["+str(threadNum)+" podo] running.. "+query+"/log_"+str(threadNum)+".txt"
		os.system(query+"/log_"+str(threadNum)+".txt")

def allDevices(cbe,caf,atype):
	threads = []
	for i in range(len(data)):
		tmp = data[i].find('\t')
		data[i] = data[i][:tmp]
		q=cbe+data[i]+caf
		t = threading.Thread(target=runThread,args=(q,atype,i,))
		t.start()	
	for t in threads:
		t.join()
	raw_input("Press any key.\n")

def singleDevice(cbe,caf,atype):
	if(atype != "choice"):
		usage_choice()
	
	for i in range(len(data)):
		tmp = data[i].find('\t')
		data[i] = data[i][:tmp]
		print " ["+str(i)+"]  ->  "+data[i] 
	print "-------------------------------------------------------------"
	number = raw_input("CMD>: ")
	
	nowtime = datetime.today().strftime("%Y%m%d%H%M%s")
	dirname = './log/'+nowtime
	if not os.path.isdir(dirname):
		os.mkdir(dirname)
	
	if(atype == "log"):
		q=cbe+data[int(number)]+" logcat -v time -b main -d > "+dirname
		runThread(q,atype,'main')
		q=cbe+data[int(number)]+" logcat -v time -b system -d > "+dirname
		runThread(q,atype,'system')
		q=cbe+data[int(number)]+" logcat -v time -b event -d > "+dirname
		runThread(q,atype,'event')
		q=cbe+data[int(number)]+" logcat -v time -b radio -d > "+dirname
		runThread(q,atype,'radio')
	else:
		q=cbe+data[int(number)]+caf
		runThread(q,atype,0)
	raw_input("Press any key.\n")

print "Load adb devices.."
os.system("adb devices")
while(1):
	usage()
	cmd = raw_input("CMD>: ")
	if(cmd == "x"):
		exit()
	elif(cmd == "1"):
		usage_1()
		cmd_1d = raw_input("CMD>: ")
		if(cmd_1d == "1"):
			singleDevice("adb -s "," install ","apk")
		elif(cmd_1d == "2"):
			allDevices("adb -s "," install ","apk")
		elif(cmd_1d == "x"):
			pass
		
	elif(cmd == "2"):
		usage_2()
		cmd_1d = raw_input("CMD>: ")
		if(cmd_1d == "1"):
			singleDevice("adb -s "," logcat ","log")
		elif(cmd_1d == "2"):
			allDevices("adb -s "," logcat -v","log")
		elif(cmd_1d == "x"):
			pass
	elif(cmd == "3"):
		listOfDevices()	
		result = 0
	



