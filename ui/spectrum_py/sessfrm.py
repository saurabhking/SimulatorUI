#from settings import SessionID, SETUP
import settings
SETUPStr = ''
SessionHeader = ''
P1_DSMCC_header = '110240104c212a3dff0000b4'
P2_Session_id = ''
P3_Reserved = '0000'
P4_ClientNSAP = ''
P5_ServerNSAP = '2d00000000000000000000000000000000000000'
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
catID = '63617449643D343030313534333B'
#tsid = ''
#ctec_tsid = '747369643d34303637333b'
headend = ''
assetId = ''
providerId = ''
startTime = ''
#odaStr = '6F64613D61766E3B6E70743D303B'
#odaStr = '6F64613D61766E3B6E70743D313030303B'
#odaStr = '6f64613d61766e3b6e70743d3632303030303b'
import pymongo
from pymongo import MongoClient

macId = ''
assetT = ''

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
	print P4_ClientNSAP		

#Function to generate delivery id
def generateDeliveryId(mac,deliveryid,npt,headend,s_tsid):
	global headEndID
	headEndID = headend
	global deliveryID
	global deliveryIDStr
	generateClientNSAP(mac,headEndID)
	deliveryIDStr = 'deliveryId=' + deliveryid + ';'
	print deliveryIDStr
	deliveryID = ''.join(x.encode('hex') for x in deliveryIDStr)
	odaStr = '6f64613d61766e3b6e70743d' + settings.asctohex(npt) +'3b'
	#global tsid
	tsid = '747369643d' + settings.asctohex(s_tsid) +'3b'
	print("============================================>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",tsid)
	global catID
	global P7_UserData_ARDData
	P7_UserData_ARDData = odaStr +  tsid + deliveryID
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
	UserPvtData = P7_UserData_ProtocolId + P7_UserData_Version + P7_UserData_DescCount + P7_UserData_NodeGrpIDTAG + P7_UserData_NodeGrpIDLen + P7_UserData_NodeGrpIDData + P7_UserData_ARDTag + P7_UserData_ARDLength + P7_UserData_ARDData + '0108000000010000000100'
	P7_UserData_pvtDataLengthex = len(UserPvtData)/2
	P7_UserData_pvtDataLengthStr = hex(P7_UserData_pvtDataLengthex)
	P7_UserData_pvtDataLength = format(P7_UserData_pvtDataLengthex,'04x')
	P6_UserData = P7_UserData_datalength + P7_UserData_pvtDataLength + UserPvtData
	return;

#Function to formulate Session Header
def formSessionHeader():
	global P1_DSMCC_header
	global P2_Session_id
	P2_Session_id = settings.SessionID
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
	print SETUPStr
	settings.SETUP = SETUPStr.decode('hex')
	return;
