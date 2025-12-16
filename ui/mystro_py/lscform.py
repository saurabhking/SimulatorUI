# Script to form various LSC Messages 
# LSC_PLAY, LSC_PAUSE, LSC_FF, LSC_RWD

import settings
import pymongo
from pymongo import MongoClient
sh_sess_id = ''
shsessid = settings.Stream_handle
print shsessid
import socket

counter = 0

#server_addr="172.30.84.137"
server_addr="172.16.146.166"
#server_addr="ctec-pprd-mdms01-rdc1-fsmlscp01.rdc1.enwd.co.sa.charterlab.com"
server_port=10101
print "Connection for LSC is about to connected"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_addr, server_port))
BUFFER_SIZE = 20

def lscplay(SessionId):
	global counter
	counter += 1
	LSC1 = '01'
	LSC_TCODE = format(counter,'02x')
	LSC_OPCODE = '0600'
	LSC2 = '800000007fffffff00010001'
	LSCSTR = LSC1 + LSC_TCODE + LSC_OPCODE + shsessid + LSC2 
	#print "In LSC PLAY"
	#print LSCSTR
	initSettingsValue()
	LSC_PLAY = LSCSTR.decode('hex')
	try:
                s.sendall(LSC_PLAY)
                data = s.recv(BUFFER_SIZE)
                encodedata = data.encode('hex')
                count = 0
                while((len(encodedata) < 34)and(count < 3)):
                        print count
                        print len(encodedata)
                        data  = s.recv(BUFFER_SIZE)
                        encodedata = data.encode('hex')
                        count += 1
                if(count == 3):
                        print "No LSC PLAY response data received"
                        return "-1";
                else:
                        decryptTCPinfo(encodedata)
                        LSC_STATUS = encodedata[6:8]
                        return LSC_STATUS;
        except:
                print"In LSC PLAY Socket closed"
                return "-1"

def lscpause(SessionId):
	global counter
	counter += 1
        LSC1 = '01'
        LSC_TCODE = format(counter,'02x')
	LSC_OPCODE = '0100'
        LSC2 = '80000000'
	LSCSTR = LSC1 + LSC_TCODE + LSC_OPCODE + shsessid + LSC2
	print "In LSC PAUSE"
        print LSCSTR
	initSettingsValue()
	LSC_PAUSE = LSCSTR.decode('hex')
	try:
	        s.sendall(LSC_PAUSE)
        	data = s.recv(BUFFER_SIZE)
		encodedata = data.encode('hex')
        	count = 0
	        while((len(encodedata) < 34)and(count < 2)):
        	        print count
			print len(encodedata)
			data  = s.recv(BUFFER_SIZE)
        	        encodedata = data.encode('hex')
                	count += 1
	        if(count == 2):
        	        print "No LSC PAUSE response data received"
                	return "-1";
	        else:
        	        decryptTCPinfo(encodedata)
                	LSC_STATUS = encodedata[6:8]
	                return LSC_STATUS;
	except:
		print"In LSC Pause Socket closed"
		return "-1"

def lscfwd(SessionId):
        global counter
        counter += 1
        LSC1 = '01'
        LSC_TCODE = format(counter,'02x')
	LSC_OPCODE = '0600'
        LSC2 = '800000007fffffff00050001'
        LSCSTR = LSC1 + LSC_TCODE + LSC_OPCODE + shsessid + LSC2
	initSettingsValue()
        LSC_PLAY = LSCSTR.decode('hex')
	try:
                s.sendall(LSC_PLAY)
                data = s.recv(BUFFER_SIZE)
                encodedata = data.encode('hex')
                count = 0
                while((len(encodedata) < 34)and(count < 2)):
                        print count
                        print len(encodedata)
                        data  = s.recv(BUFFER_SIZE)
                        encodedata = data.encode('hex')
                        count += 1
                if(count == 2):
                        print "No LSC fwd response data received"
                        return "-1";
                else:
                        decryptTCPinfo(encodedata)
                        LSC_STATUS = encodedata[6:8]
                        return LSC_STATUS;
        except:
                print"In LSC fwd Socket closed"
                return "-1"
def lscfwd_2x(SessionId):
        global counter
        counter += 1
        LSC1 = '01'
        LSC_TCODE = format(counter,'02x')
        LSC_OPCODE = '0600'
        LSC2 = '800000007fffffff000f0001'
        LSCSTR = LSC1 + LSC_TCODE + LSC_OPCODE + shsessid + LSC2
        print "In LSC Fwd 2X"
        print LSCSTR
        initSettingsValue()
        LSC_PLAY = LSCSTR.decode('hex')
        s.sendall(LSC_PLAY)
        data = s.recv(BUFFER_SIZE)
        encodedata = data.encode('hex')
        count = 0
        while((len(encodedata) <  34)and(count < 2)):
                data  = s.recv(BUFFER_SIZE)
                encodedata = data.encode('hex')
                count += 1
        if(count == 2):
                print "No LSC FWD response data received"
                return "-1";
        else:
                print encodedata
                decryptTCPinfo(encodedata)
                LSC_STATUS = encodedata[6:8]
                return LSC_STATUS;

def lscfwd_3x(SessionId):
        global counter
        counter += 1
        LSC1 = '01'
        LSC_TCODE = format(counter,'02x')
        LSC_OPCODE = '0600'
        LSC2 = '800000007fffffff001e0001'
        LSCSTR = LSC1 + LSC_TCODE + LSC_OPCODE + shsessid + LSC2
        print "In LSC Fwd 3X"
        print LSCSTR
        initSettingsValue()
        LSC_PLAY = LSCSTR.decode('hex')
        s.sendall(LSC_PLAY)
        data = s.recv(BUFFER_SIZE)
        encodedata = data.encode('hex')
        count = 0
        while((len(encodedata) <  34)and(count < 2)):
                data  = s.recv(BUFFER_SIZE)
                encodedata = data.encode('hex')
                count += 1
        if(count == 2):
                print "No LSC FWD response data received"
                return "-1";
        else:
                print encodedata
                decryptTCPinfo(encodedata)
                LSC_STATUS = encodedata[6:8]
                return LSC_STATUS;

def lscfwd_4x(SessionId):
        global counter
        counter += 1
        LSC1 = '01'
        LSC_TCODE = format(counter,'02x')
        LSC_OPCODE = '0600'
        LSC2 = '800000007fffffff003c0001'
        LSCSTR = LSC1 + LSC_TCODE + LSC_OPCODE + shsessid + LSC2
        print "In LSC Fwd 4X"
        print LSCSTR
        initSettingsValue()
        LSC_PLAY = LSCSTR.decode('hex')
        s.sendall(LSC_PLAY)
        data = s.recv(BUFFER_SIZE)
        encodedata = data.encode('hex')
        count = 0
        while((len(encodedata) <  34)and(count < 2)):
                data  = s.recv(BUFFER_SIZE)
                encodedata = data.encode('hex')
                count += 1
        if(count == 2):
                print "No LSC FWD response data received"
                return "-1";
        else:
                print encodedata
                decryptTCPinfo(encodedata)
                LSC_STATUS = encodedata[6:8]
                return LSC_STATUS;


def lscrwd(SessionId):
        global counter
        counter += 1
        LSC1 = '01'
        LSC_TCODE = format(counter,'02x')
	LSC_OPCODE = '0600'
        LSC2 = '800000007ffffffffffb0001'
        LSCSTR = LSC1 + LSC_TCODE + LSC_OPCODE + shsessid + LSC2
        #print "In LSC RWD"
        #print LSCSTR
	initSettingsValue()
        LSC_PLAY = LSCSTR.decode('hex')
	try:
                s.sendall(LSC_PLAY)
                data = s.recv(BUFFER_SIZE)
                encodedata = data.encode('hex')
                count = 0
                while((len(encodedata) < 34)and(count < 2)):
                        print count
                        print len(encodedata)
                        data  = s.recv(BUFFER_SIZE)
                        encodedata = data.encode('hex')
                        count += 1
                if(count == 2):
                        print "No LSC rwd response data received"
                        return "-1";
                else:
                        decryptTCPinfo(encodedata)
                        LSC_STATUS = encodedata[6:8]
                        return LSC_STATUS;
        except:
                print"In LSC rwd Socket closed"
                return "-1"
def lscrwd_2x(SessionId):
        global counter
        counter += 1
        LSC1 = '01'
        LSC_TCODE = format(counter,'02x')
        LSC_OPCODE = '0600'
        LSC2 = '800000007ffffffffff10001'
        LSCSTR = LSC1 + LSC_TCODE + LSC_OPCODE + shsessid + LSC2
        print "In LSC RWD 2X"
        print LSCSTR
        initSettingsValue()
        LSC_PLAY = LSCSTR.decode('hex')
        s.sendall(LSC_PLAY)
        data = s.recv(BUFFER_SIZE)
        encodedata = data.encode('hex')
        count = 0
        while((len(encodedata) < 34)and(count < 2)):
                data  = s.recv(BUFFER_SIZE)
                encodedata = data.encode('hex')
                count += 1
        if(count == 2):
                print "No LSC RWD  response data received"
                return "-1";
        else:
                print encodedata
                decryptTCPinfo(encodedata)
                LSC_STATUS = encodedata[6:8]
                return LSC_STATUS;

def lscrwd_3x(SessionId):
        global counter
        counter += 1
        LSC1 = '01'
        LSC_TCODE = format(counter,'02x')
        LSC_OPCODE = '0600'
        LSC2 = '800000007fffffffffe20001'
        LSCSTR = LSC1 + LSC_TCODE + LSC_OPCODE + shsessid + LSC2
        print "In LSC RWD 3X"
        print LSCSTR
        initSettingsValue()
        LSC_PLAY = LSCSTR.decode('hex')
        s.sendall(LSC_PLAY)
        data = s.recv(BUFFER_SIZE)
        encodedata = data.encode('hex')
        count = 0
        while((len(encodedata) < 34)and(count < 2)):
                data  = s.recv(BUFFER_SIZE)
                encodedata = data.encode('hex')
                count += 1
        if(count == 2):
                print "No LSC RWD  response data received"
                return "-1";
        else:
                print encodedata
                decryptTCPinfo(encodedata)
                LSC_STATUS = encodedata[6:8]
                return LSC_STATUS;

def lscrwd_4x(SessionId):
        global counter
        counter += 1
        LSC1 = '01'
        LSC_TCODE = format(counter,'02x')
        LSC_OPCODE = '0600'
        LSC2 = '800000007fffffffffc40001'
        LSCSTR = LSC1 + LSC_TCODE + LSC_OPCODE + shsessid + LSC2
        print "In LSC RWD 4X"
        print LSCSTR
        initSettingsValue()
        LSC_PLAY = LSCSTR.decode('hex')
        s.sendall(LSC_PLAY)
        data = s.recv(BUFFER_SIZE)
        encodedata = data.encode('hex')
        count = 0
        while((len(encodedata) < 34)and(count < 2)):
                data  = s.recv(BUFFER_SIZE)
                encodedata = data.encode('hex')
                count += 1
        if(count == 2):
                print "No LSC RWD  response data received"
                return "-1";
        else:
                print encodedata
                decryptTCPinfo(encodedata)
                LSC_STATUS = encodedata[6:8]
                return LSC_STATUS;



def lscstatus(SessionId):
	global counter
        counter += 1
	LSC1 = '01'
        LSC_TCODE = format(counter,'02x')
	LSC_OPCODE = '0300'
	LSCSTR = LSC1 + LSC_TCODE + LSC_OPCODE + shsessid
       	print "In LSC STATUS"
        print LSCSTR
	initSettingsValue()
	LSC_STATUS = LSCSTR.decode('hex')
	try:
	        s.sendall(LSC_STATUS)
		data = s.recv(BUFFER_SIZE)
		encodedata = data.encode('hex')
		print encodedata
		print len(encodedata)
		count = 0
		while((len(encodedata) < 34)and(count < 2)): 
			data  = s.recv(BUFFER_SIZE)
			encodedata = data.encode('hex')
			print encodedata
		        print len(encodedata)
			count += 1
		if(count == 2):
        	        print "No LSC STATUS response data received"
                	return "-1";
	        else:
			decryptTCPinfo(encodedata)
        		LSC_STATUS = encodedata[6:8]
		        return LSC_STATUS;
	except:
		print" Socket Timedout"
		return "-1"

def decryptOpcode(opcode):
	if(opcode == '81'):
		return 'LSC_PAUSE_REPLY';
	elif(opcode == '82'):
		return 'LSC_RESUME_REPLY';
	elif(opcode == '83'):
		return 'LSC_STATUS_REPLY';
	elif(opcode == '84'):
                return 'LSC_RESET_REPLY';
        elif(opcode == '85'):
                return 'LSC_JUMP_REPLY';
	elif(opcode == '86'):
                return 'LSC_PLAY_REPLY';
	else:
		return opcode;

def decryptScale(scalenum, scaledeno):
	if((scalenum != '')and(scaledeno != '')):
		num = int(scalenum, 16)
		deno = int(scaledeno,16)
		scale = num/deno;
		#print num
		#print deno
		#print scale
		if ((num == 1)and(deno ==1)):
			return "PLAY"
		elif((num == 0)):
			return "PAUSE"
	
		elif((num > deno)and ( num < 0xA)):
			return "FFWD 5X "
		elif((num > deno)and ( num < 0x14)):
                        return "FFWD 15X"
                elif((num > deno)and ( num < 0x28)):
                        return "FFWD 30X"
       		elif((num > deno)and ( num < 0x46)):
                        return "FFWD 60X"
	     	elif((num > 0xFFFA)and(num > deno)):
			return "RWD 5X"
                elif((num > 0xFFF0)and(num > deno)):
                        return "RWD 15X "
	        elif((num > 0xFFE1)and(num > deno)):
                        return "RWD 30X "
		elif((num > 0xFFC3)and(num > deno)):
                        return "RWD 60X "

		else:
			return 

def decryptTCPinfo(tcpResponse):
        opcode  = tcpResponse[4:6]
        settings.LSC_OPCODE = decryptOpcode(opcode)	
        print settings.LSC_OPCODE
	settings.LSC_status = tcpResponse[6:8]
        settings.LSC_CNPT = tcpResponse[16:24]
	print "Current NPT"
        print settings.LSC_CNPT
	scalenum  = tcpResponse[24:28]
        print "Scale Num"
        print scalenum
        scaledeno = tcpResponse[28:32]
	settings.LSC_SCALE_NUM = decryptScale(scalenum,scaledeno)
	print settings.LSC_SCALE_NUM
        settings.LSC_MODE = tcpResponse[32:34]

def initSettingsValue():
	settings.LSC_OPCODE = ''
	settings.LSC_status = '-1'
	settings.LSC_CNPT = ''
	settings.LSC_SCALE_NUM = ''
	settings.LSC_MODE = ''

def closeSocket():
	s.close()
