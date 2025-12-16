import socket
import os
import subprocess
import shlex
import ConfigParser
import sys
import time
import datetime
import settings
#import sendMessage
import statusResponse
import csv
import requests
#import  datafiles 
import paramiko
#uri = ''
#global uri
global Global_id
Global_id = ''
def read_config_file(conf_file):
         try:
            config=ConfigParser.ConfigParser()
            with open(conf_file,'r') as conf_file:
                config.readfp(conf_file)
            return config
         except Exception as e:
            print e
         conf=read_config_file('mdms-IP.cfg')
         print "End of config file"

timestamp=str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H:%M:%S'))

currd = os.getcwd()
print currd

import os.path
print "Shud print parent directory"
pDir = os.path.abspath(os.path.join(currd, os.pardir))
#def healthchk(session):
def healthchk():
        try: 
	    myfile = open(pDir + "healthchk_mystro.csv", 'wb')
	    
	    wr = csv.writer(myfile)
	    header = ["Healthcheck Report Proxy"]
	    healthchklist = ["Tests","Results","Notes"]
	    wr.writerow([datetime.datetime.now()])
	    wr.writerow(header)
	    wr.writerow(healthchklist)

	    #settings.findPrimaryDb()
            mac = "44e08eb97817"
	    settings.generateSessionId(mac)
	    print "Session Id generated" 
	    #offeringId = settings.getAssetId()
	    offeringId = "45896" 
	    #offeringId = "80636"
	    print "Offering Id for Health Check Test is ",offeringId
	    import  sessfrm 
	    print "Generating delivery ID"
            sessfrm.generateDeliveryId(offeringId,mac)
	   
            headEndID = sessfrm.headEndID
	    print "Delivery ID generated"
            print sessfrm.deliveryID
            sessfrm.formUserData()
            Global_DeliveryId_2 =  sessfrm.deliveryIDStr
            Global_id =  Global_DeliveryId_2[11:] 
	    #sessfrm.formUserData()
	    sessfrm.formSessionHeader()
	    sessfrm.formSetupMsg()
        except Exception as e:
          print str(e)
          #healthchklist.append(str(e))
        try:
		healthchklist = []
		healthchklist.append("Session Setup")
		import sendMessage
		status = sendMessage.initiateSetupSession()
		print status
		if(int(status,16) == 0):
			healthchklist.append("PASS")
		else:
			healthchklist.append("FAIL")
		response = statusResponse.setupResponse(int(status,16))
		healthchklist.append(response)
		wr.writerow(healthchklist)
   		sendMessage.sendHeartBeatMsg()
		#print "Printing sendMessage"
        except Exception as e:
          print str(e)
	  healthchklist.append("FAIL")
          healthchklist.append(str(e))
          #wr.writerow(healthchklist)

	#import lscform
        #def lsccommands():
	
        import lscform
	#if int(status) == 0: 
        try:
            if (int(status,16) == 0):
		healthchklist = []
		healthchklist.append("LSC STATUS")
		lsc_status = lscform.lscstatus(settings.SessionID)
		if(int(lsc_status,16) == 0):
			healthchklist.append("PASS")
		else:
			healthchklist.append("FAIL")
		response = statusResponse.lscResponse(int(lsc_status,16))
		healthchklist.append(response)
		wr.writerow(healthchklist)

	        healthchklist = []
		healthchklist.append("LSC PAUSE")
		lsc_status = lscform.lscpause(settings.SessionID)
		if(int(lsc_status,16) == 0):
        		healthchklist.append("PASS")
		else:
        		healthchklist.append("FAIL")
		response = statusResponse.lscResponse(int(lsc_status,16))
		healthchklist.append(response)
		wr.writerow(healthchklist)

		healthchklist = []
		healthchklist.append("LSC PLAY")
		lsc_status = lscform.lscplay(settings.SessionID)
		if(int(lsc_status,16) == 0):
        		healthchklist.append("PASS")
		else:
        		healthchklist.append("FAIL")
		response = statusResponse.lscResponse(int(lsc_status,16))
		healthchklist.append(response)
		wr.writerow(healthchklist)
		
		healthchklist = []
		healthchklist.append("LSC FWD5X")
		lsc_status = lscform.lscfwd(settings.SessionID)
		if(int(lsc_status,16) == 0):
        		healthchklist.append("PASS")
		else:
        		healthchklist.append("FAIL")
		response = statusResponse.lscResponse(int(lsc_status,16))
		healthchklist.append(response)
		wr.writerow(healthchklist)

		healthchklist = []
		healthchklist.append("LSC FWD15X")
		lsc_status = lscform.lscfwd_2x(settings.SessionID)
		if(int(lsc_status,16) == 0):
        		healthchklist.append("PASS")
		else:
        		healthchklist.append("FAIL")
		response = statusResponse.lscResponse(int(lsc_status,16))
		healthchklist.append(response)
		wr.writerow(healthchklist)

		healthchklist = []
		healthchklist.append("LSC FWD30X")
		lsc_status = lscform.lscfwd_3x(settings.SessionID)
		if(int(lsc_status,16) == 0):
        		healthchklist.append("PASS")
		else:
        		healthchklist.append("FAIL")
		response = statusResponse.lscResponse(int(lsc_status,16))
		healthchklist.append(response)
		wr.writerow(healthchklist)

		healthchklist = []
		healthchklist.append("LSC FWD60X")
		lsc_status = lscform.lscfwd_4x(settings.SessionID)
		if(int(lsc_status,16) == 0):
        		healthchklist.append("PASS")
		else:
        		healthchklist.append("FAIL")
		response = statusResponse.lscResponse(int(lsc_status,16))
		healthchklist.append(response)
		wr.writerow(healthchklist)

		healthchklist = []
		healthchklist.append("LSC PLAY")
		lsc_status = lscform.lscplay(settings.SessionID)
		if(int(lsc_status,16) == 0):
        		healthchklist.append("PASS")
		else:
        		healthchklist.append("FAIL")
		response = statusResponse.lscResponse(int(lsc_status,16))
		healthchklist.append(response)
		wr.writerow(healthchklist)

		healthchklist = []
		healthchklist.append("LSC RWD5X")
		lsc_status = lscform.lscrwd(settings.SessionID)
		if(int(lsc_status,16) == 0):
        		healthchklist.append("PASS")
		else:
        		healthchklist.append("FAIL")
		response = statusResponse.lscResponse(int(lsc_status,16))
		healthchklist.append(response)
		wr.writerow(healthchklist)

		healthchklist = []
		healthchklist.append("LSC RWD15X")
		lsc_status = lscform.lscrwd_2x(settings.SessionID)
		if(int(lsc_status,16) == 0):
        		healthchklist.append("PASS")
		else:
        		healthchklist.append("FAIL")
		response = statusResponse.lscResponse(int(lsc_status,16))
		healthchklist.append(response)
		wr.writerow(healthchklist)

		healthchklist = []
		healthchklist.append("LSC RWD30X")
		lsc_status = lscform.lscrwd_3x(settings.SessionID)
		if(int(lsc_status,16) == 0):
        		healthchklist.append("PASS")
		else:
        		healthchklist.append("FAIL")
		response = statusResponse.lscResponse(int(lsc_status,16))
		healthchklist.append(response)
		wr.writerow(healthchklist)

		healthchklist = []
		healthchklist.append("LSC RWD60X")
		lsc_status = lscform.lscrwd_4x(settings.SessionID)
		if(int(lsc_status,16) == 0):
       			 healthchklist.append("PASS")
		else:
        		healthchklist.append("FAIL")
		response = statusResponse.lscResponse(int(lsc_status,16))
		healthchklist.append(response)
		wr.writerow(healthchklist)

		healthchklist = []
		healthchklist.append("LSC PLAY")
		lsc_status = lscform.lscplay(settings.SessionID)
		if(int(lsc_status,16) == 0):
        		healthchklist.append("PASS")
		else:
        		healthchklist.append("FAIL")
		response = statusResponse.lscResponse(int(lsc_status,16))
		healthchklist.append(response)
		wr.writerow(healthchklist)	
           
            	
            else:
            	print "LSC Status Fail"
            	healthchklist = []
	    	healthchklist.append("LSC STATUS")
            	healthchklist.append("FAIL")
            	wr.writerow(healthchklist)
            	healthchklist = []
            	healthchklist.append("LSC PAUSE")
            	healthchklist.append("FAIL")
            	wr.writerow(healthchklist)
            	healthchklist = []
            	healthchklist.append("LSC PLAY")
            	healthchklist.append("FAIL")
            	wr.writerow(healthchklist)
            	healthchklist = []
            	healthchklist.append("LSC FWD5X")
            	healthchklist.append("FAIL")
            	wr.writerow(healthchklist)
            	healthchklist = []
            	healthchklist.append("LSC FWD15X")
            	healthchklist.append("FAIL")
            	wr.writerow(healthchklist)
            	healthchklist = []
            	healthchklist.append("LSC FWD30X")
            	healthchklist.append("FAIL")
            	wr.writerow(healthchklist)
            	healthchklist = []
            	healthchklist.append("LSC FWD60X")
            	healthchklist.append("FAIL")
            	wr.writerow(healthchklist)
            	healthchklist = []
            	healthchklist.append("LSC PLAY")
            	healthchklist.append("FAIL")
            	wr.writerow(healthchklist)
            	healthchklist = []
            	healthchklist.append("LSC RWD5X")
            	healthchklist.append("FAIL")
            	wr.writerow(healthchklist)
            	healthchklist = []
            	healthchklist.append("LSC RWD15X")
            	healthchklist.append("FAIL")
            	wr.writerow(healthchklist)
            	healthchklist = []
            	healthchklist.append("LSC RWD30X")
           	healthchklist.append("FAIL")
            	wr.writerow(healthchklist)
            	healthchklist = []
            	healthchklist.append("LSC RWD60X")
            	healthchklist.append("FAIL")
            	wr.writerow(healthchklist)
            	healthchklist = []
            	healthchklist.append("LSC PLAY")
            	healthchklist.append("FAIL")
            	wr.writerow(healthchklist)
            
        except Exception as e:
             print str(e)
             healthchklist.append(str(e))
	import tearform
        try: 
		healthchklist = []
		healthchklist.append("TEARDOWN")
		teardown_status=sendMessage.sendTearDownMsg()
		if(int(teardown_status,16) == 0):
			healthchklist.append("PASS")
		else:
			healthchklist.append("FAIL")
		wr.writerow(healthchklist)

		#healthchklist = []
		#healthchklist.append("Connectivity Tests")
        except Exception as e:
	        print str(e)
	        healthchklist.append(str(e))
         	wr.writerow(healthchklist)

healthchk()
