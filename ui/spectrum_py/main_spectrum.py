# Script to run proxy health check


import time
import xml.etree.ElementTree as ET
import ConfigParser
import requests
import json
import settings
import sendMessage
import statusResponse
import sessfrm  
import lscform
active = False
sessionid = ''


def start(dsmcc_host,lsc_host,mac,deliveryId,npt,headend,tsid):
	try:
		global active
		global sessionid
		settings.dsmcc_host = dsmcc_host
		settings.lsc_host = lsc_host
		settings.SessionID = settings.generateSessionId(mac)
		sessionid = settings.SessionID
		settings.findPrimaryDb()
		sessfrm.generateDeliveryId(mac,deliveryId,npt,headend,tsid)
		sessfrm.formUserData()
		sessfrm.formSessionHeader()
		sessfrm.formSetupMsg()
		lscform.init()
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
			lscform.lscstatus()
			time.sleep(59)
		except Exception as e:
			print("error while sending heartbeat and status")


def play():
	response = ''
	try:
		if(active):
			lsc_status = lscform.lscplay()
			response = statusResponse.lscResponse(int(lsc_status,16))
			print("Play ..............................",response)
		return lsc_status
	except Exception as e:
		print str(e)
		return lsc_status

		
def pause():
	response = ''
	try:
		if(active):
			lsc_status = lscform.lscpause()
			response = statusResponse.lscResponse(int(lsc_status,16))
			print("pause ..............................",response)
		return lsc_status
	except Exception as e:
		print str(e)
		return lsc_status


def ff():
	response = ''
	try:
		if(active):
			lsc_status = lscform.lscfwd()
			response = statusResponse.lscResponse(int(lsc_status,16))
			print("fast forward ..............................",response)
		return lsc_status
	except Exception as e:
		print str(e)
		return lsc_status

		
def rw():
	response = ''
	try:
		if(active):
			lsc_status = lscform.lscrwd()
			response = statusResponse.lscResponse(int(lsc_status,16))
			print("rewind ..............................",response)
		return lsc_status
	except Exception as e:
		print str(e)
		return lsc_status		


def teardown():
	try:
		global active
		active = False
		teardown_status=sendMessage.sendTearDownMsg()
	except Exception as e:
		print str(e)

		
def get_account(mac,setting_api_host,headend):
	try:
		print "Get Account Info"
		url = "http://"+setting_api_host+":8000/vod/accountInfo?deviceId="+mac+"&headendId="+headend
		print url
		r = requests.get(url)
		print r.text
		print r.status_code
		if(r.status_code == 200):
			rentals = []
			root = ET.fromstring(r.text)
			for rental in root.iter('Rental'):
				title = rental.get('title')
				deliveryId = rental.get('deliveryId')
				npt = rental.get('npt')
				datum = {"name": title, "id": deliveryId, "npt": npt}
				rentals.append(datum)
			return rentals
		else:
			return ""
		
	except Exception as e:
		print str(e)
		return ""



