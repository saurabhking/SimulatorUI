# To maintain global varibales that will be needed across project

SessionID = ''
SETUP = ''
Stream_handle = ''
uri = ''
dsmcc_host = ''
lsc_host = ''
#Function to make a SessionId
import random
def generateSessionId(mac):
	sessionId = random.randint(1, 1000000)
	hexno = format(sessionId, '08x')
	global SessionID
	SessionID = mac  + hexno
	print ("SessionID",SessionID)
	return SessionID;


import pymongo
from pymongo import MongoClient
# Function to get the primary db uri 
def findPrimaryDb():
        global uri
        uri = "mongodb://admin:admin1234@172.16.146.84:27017/?authMechanism=SCRAM-SHA-1"
        print "Primary Mongo DB URI"
        print uri

def getAssetId():
        global uri
        uri = findPrimaryDb()
        uri = "mongodb://admin:admin1234@172.16.146.84:27017/?authMechanism=SCRAM-SHA-1"
        connection = MongoClient(uri)
        db = connection.MONACODB
        listquery = db.offerings.find({'status':'active'},{'offering_id':1,"_id":0})
        refoid = 0
        for oid in listquery:
                print oid
                refoid =  oid['offering_id']
                print refoid
                return refoid

def asctohex(string_in):
	a=""
	for x in string_in:
		a = a + ("0"+((hex(ord(x)))[2:]))[-2:]
	return(a)
	
#session setup status
SETUP_status=False
HEARTBEAT_status=False
TEARDOWN_status=False
LSC_PLAY_status=False
LSC_PAUSE_status=False
LSC_STATUS_status=False

SETUP_status_code=''
HEARTBEAT_status_code=''
TEARDOWN_status_code=''

LSC_OPCODE = ''
LSC_status = ''
LSC_CNPT = ''
LSC_SCALE_NUM = ''
LSC_SCALE_DENO = ''
LSC_MODE = ''
