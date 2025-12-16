# To maintain global varibales that will be needed across project

SessionID = ''
SETUP = ''
Stream_handle = ''
uri = ''
dsmcc_host = 'mdms-int01-dsmcc-ndc.sa.g.charterlab.com'
#Function to make a SessionId
import random
def generateSessionId(mac):
        sessionId = random.randint(1, 1000000)
        hexno = format(sessionId, '08x')
        global SessionID
        SessionID = mac  + hexno
	#SessionID = '00000083749c350ec0a9'
	print "SessionID = "+SessionID 
	#print SessionID
        return;


import pymongo
from pymongo import MongoClient
# Function to get the primary db uri 
def findPrimaryDb():
        global uri
        uri = "mongodb://admin:admin1234@172.16.146.84:27017/?authMechanism=SCRAM-SHA-1"
        #uri = "mongodb://admin:admin1234@172.16.146.84:27020"
        print "Primary Mongo DB URI"
        return uri


def getAssetId():
        #global uri
        uri = findPrimaryDb()
        print uri
	connection = MongoClient(uri)
	db = connection.ADAPTERDB
        listquery = db.openstream_offerings.find({'headendId':'ctec_a3h1','serviceName':'Video Store','createTime': {"$gt": "2017-05-19T20:51:05Z"}},{'offeringId':1,"_id":0,'headendId':1,'expirationDate':1})
        #listquery = db.openstream_offerings.find({'movieAsset.runTime':{"$gt": 6000},'serviceName':'EXP_BASIC'},{'offeringId':1,"_id":0,'headendId':1})
	#listquery = db.openstream_offerings.find({'movieAsset.runTime':{"$gt": 6000},'serviceName':'Latino View'},{'offeringId':1,"_id":0,'headendId':1})
        refoid = 0
        for oid in listquery:
                refoid =  oid['offeringId']
                #dgoid =  refoid / 100
                dhendId = oid['headendId']
		exDate = oid['expirationDate']
		print exDate
		print dhendId	
		import datetime
                currDate = datetime.datetime.now().isoformat()	
                if((dhendId == 'ctec_a3h1')and(exDate >= currDate)):
                        print dhendId
                        break;

        offeringId = refoid
        #offeringId = dgoid
	#print offeringId
        return offeringId
        #offeringId = listquery['offeringId']
        #return offeringId



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
