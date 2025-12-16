#from settings_ndc1 import SessionID, SETUP
import json
import settings
SETUPStr = ''
SessionHeader = ''
P1_DSMCC_header = '1102401049c6250bff0000b9'
P2_Session_id = settings.SessionID             # Generate from MAC and Random No. 
print P2_Session_id
P3_Reserved = '0000'
P4_ClientNSAP = ''
P5_ServerNSAP = '2d00000000000000000a0a0a0a00000000000000'
P6_UserData = ''
P7_UserData_datalength = '0000' 
P7_UserData_pvtDataLength = ''   # To be Calculated
P7_UserData_ProtocolId = '01'
P7_UserData_Version  = '00'
P7_UserData_DescCount = '02'
P7_UserData_NodeGrpIDTAG = '02' 
P7_UserData_NodeGrpIDLen = '06'
P7_UserData_NodeGrpIDData = '000000000000'
P7_UserData_ARDTag      = '05'
P7_UserData_ARDLength   = ''
P7_UserData_ARDData     = ''
deliveryID = ''
catID = '63617449643d3137353835303b'
headend = ''
assetId = ''
providerId = ''
startTime = ''
odaStr = '6F64613D61766E3B6E70743D303B'

import pymongo
from pymongo import MongoClient

macId = ''
assetT = ''

#Client NSAP is hardcoded for mystro script
def generateClientNSAP(mac,headendId):
         import socket
	 ipaddr = socket.gethostbyname(socket.gethostname())
	 print ipaddr
	 nsapstr1 = "2d0000000000000000"
	 import binascii
	 import socket
	 ip = binascii.hexlify(socket.inet_aton(ipaddr))
	 print ip		
	 global P4_ClientNSAP
	 P4_ClientNSAP = nsapstr1 + ip + '00'+mac[2:12] + '00'
	 P4_ClientNSAP = '2d00000000000000000000000044e08eb9781700'
	 print P4_ClientNSAP		

#Function to generate delivery id
def generateDeliveryId(mac,deliveryid,headend):
	global catID
	global headEndID
	global deliveryID
	global deliveryIDStr
	global P7_UserData_ARDData
	headEndID = headend 
	deliveryIDStr = 'deliveryId=' + deliveryid + ';'
	print deliveryIDStr
	generateClientNSAP(mac,headEndID)
	deliveryID = ''.join(x.encode('hex') for x in deliveryIDStr)
	serviceAreaStr = 'serviceArea=10000;'
	serviceASt = ''.join(x.encode('hex') for x in serviceAreaStr)
	videoDecStr = 'videoDecodeType=0001;'
	videoDSt = ''.join(x.encode('hex') for x in videoDecStr)
	P7_UserData_ARDData = catID + deliveryID + serviceASt + videoDSt
	P7_UserData_ARDLengthex = len(P7_UserData_ARDData)/2
	global P7_UserData_ARDLength
	P7_UserData_ARDLength = format(P7_UserData_ARDLengthex,'x')
	return;


#Function to formulate User Data
def formUserData():
	global P6_UserData
	global P7_UserData_datalength
	global P7_UserData_pvtDataLength
	global P7_UserData_ProtocolId
	global P7_UserData_Version
	global P7_UserData_DescCount
	global P7_UserData_NodeGrpIDTAG
	global P7_UserData_NodeGrpIDLen
	global P7_UserData_NodeGrpIDData
	global P7_UserData_ARDTag
	global P7_UserData_ARDLength
	global P7_UserData_ARDData
	UserPvtData = P7_UserData_ProtocolId + P7_UserData_Version + P7_UserData_DescCount + P7_UserData_NodeGrpIDTAG + P7_UserData_NodeGrpIDLen + P7_UserData_NodeGrpIDData + P7_UserData_ARDTag + P7_UserData_ARDLength + P7_UserData_ARDData
	P7_UserData_pvtDataLengthex = len(UserPvtData)/2
	P7_UserData_pvtDataLengthStr = hex(P7_UserData_pvtDataLengthex)
	P7_UserData_pvtDataLength = format(P7_UserData_pvtDataLengthex,'04x')
	P6_UserData = P7_UserData_datalength + P7_UserData_pvtDataLength + UserPvtData
	return;

#Function to formulate Session Header
def formSessionHeader():
	global P1_DSMCC_header
	global P2_Session_id
	global P3_Reserved
	global P4_ClientNSAP
	global P5_ServerNSAP
	global SessionHeader
	SessionHeader = P1_DSMCC_header + P2_Session_id + P3_Reserved + P4_ClientNSAP + P5_ServerNSAP
	return;

#Function to form SETUP Message
def formSetupMsg():
	global SETUPStr
	global SETUP
	global SessionHeader
	global P6_UserData
	SETUPStr = SessionHeader + P6_UserData
	print "Steupstr = " + SETUPStr
	settings.SETUP = SETUPStr.decode('hex')
	return;





