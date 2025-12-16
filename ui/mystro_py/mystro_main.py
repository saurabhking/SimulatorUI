import socket
import os
import subprocess
import shlex
import ConfigParser
import sys
import time
import datetime
import settings
import statusResponse
import csv
import requests
import os.path
import sendMessage
import  sessfrm 
import lscform
import tearform
active = False



def play(host,mac,deliveryId,headend,tsid):
	try:
		global active
		settings.dsmcc_host = host
		settings.generateSessionId(mac)
		print "Session Id generated" 
		print "Generating delivery ID"
		sessfrm.generateDeliveryId(mac,deliveryId,headend)
		print "Delivery ID generated"
		sessfrm.formUserData()
		sessfrm.formSessionHeader()
		sessfrm.formSetupMsg()
	except Exception as e:
		print str(e)

	try:
		status = sendMessage.initiateSetupSession()
		print status
		response = statusResponse.setupResponse(int(status,16))
		if (int(status,16) == 0):
			active = True
		else:
			active = False
	except Exception as e:
		print str(e)
	
	while(active):
		try:	
			sendMessage.sendHeartBeatMsg()
			lscform.lscstatus(settings.SessionID)
			time.sleep(59)
		except Exception as e:
			print("error while sending heartbeat and status")
	
def pause():
	try: 
		if(active):
			lsc_status = lscform.lscpause(settings.SessionID)
			response = statusResponse.lscResponse(int(lsc_status,16))
	except Exception as e:
		print str(e)
	
def teardown():
	try:
		active = False
		teardown_status=sendMessage.sendTearDownMsg()
	except Exception as e:
		print str(e)

def ff():
	try:
		if(active):
			lsc_status = lscform.lscfwd(settings.SessionID)
			response = statusResponse.lscResponse(int(lsc_status,16))
	except Exception as e:
		print str(e)

def rw():
	try:
		if(active):
			lsc_status = lscform.lscrwd(settings.SessionID)
			response = statusResponse.lscResponse(int(lsc_status,16))
	except Exception as e:
		print str(e)		
