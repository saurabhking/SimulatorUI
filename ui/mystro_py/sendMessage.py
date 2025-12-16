#from timeout_wrapper import timeout
from socket import *
import time
import settings
buffer=''
global UDPSock_ssp
# Function to send SETUP Message via UDP to Core VM 1
#def read_UDP_Message(UDPSock_ssp_event):
def read_UDP_Message():
	global UDPSock_ssp
	#while UDPSock_ssp_event.is_set():
	#print "trying to read message from udp socket"
	try:
		data, addr = UDPSock_ssp.recvfrom(255)
		print "We received something on socket, please see hex encodeddata below"
		encodedata = data.encode('hex')
		print encodedata
		print "Encode data ends"
		return 0;
	except:
	        print "No Teardown data received"
		return 1;
		pass

def initiateSetupSession():
	global UDPSock_ssp
	from settings import SETUP
	# Send messages
	#mdms-vldc-dsmcc-ndc.sa.g.charterlab.com
	#host="mdms-int01-dsmcc-ndc.sa.g.charterlab.com"
	host = settings.dsmcc_host
	port = 13822
	addr = (host,port)
	UDPSock_ssp = socket(AF_INET,SOCK_DGRAM)
	if(UDPSock_ssp.sendto(SETUP,addr)):
		UDPSock_ssp.settimeout(3.0)
		try:
			recv_data, addr = UDPSock_ssp.recvfrom(990)
		        encodedata = recv_data.encode('hex')
			time.sleep(1)
                	#UDPSock_ssp.close()
        	        settings.SETUP_status_code= encodedata[44:48]
	                settings.Stream_handle = encodedata[-14:-6]
                	print settings.Stream_handle
        	        print encodedata
	                return settings.SETUP_status_code
		except timeout:
			print "Socket Timedout"
			UDPSock_ssp.close()
			return -1
        else:
		time.sleep(5)
	        UDPSock_ssp.close()
                return -1;

# Function to send HEARTBEAT Message
def sendHeartBeatMsg():
	from hbform import HEARTBEAT
	#print HEARTBEAT
	# Send messages
	#host="mdms-int01-dsmcc-ndc.sa.g.charterlab.com"
	host=settings.dsmcc_host
        port = 13822
        addr = (host,port)
        UDPSock = socket(AF_INET,SOCK_DGRAM)
        UDPSock.sendto(HEARTBEAT,addr)
	time.sleep(5)
	UDPSock.close()
	return;

# Function to send TEARDOWN Message
def sendTearDownMsg():
	from tearform import TEARDOWN
        print TEARDOWN
         # Send messages
	#host="mdms-int01-dsmcc-ndc.sa.g.charterlab.com"
	host=settings.dsmcc_host
        port = 13822
        addr = (host,port)
        UDPSock = socket(AF_INET,SOCK_DGRAM)
	if(UDPSock.sendto(TEARDOWN,addr)):
		UDPSock.settimeout(10.0)
                try:
                        recv_data, addr = UDPSock.recvfrom(255)
                        encodedata = recv_data.encode('hex')
                        time.sleep(5)
                        UDPSock.close()
                        settings.SETUP_status_code= encodedata[44:48]
                        print encodedata
                        return settings.SETUP_status_code
                except timeout:
                        print "Socket Timedout"
                        UDPSock.close()
                        return -1
        else:
                time.sleep(5)
                UDPSock.close()
                return -1;
