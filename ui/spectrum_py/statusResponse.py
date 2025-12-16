def setupResponse(status):
	if(status == 0):
		return "RspOK Request;completed without errors"
	elif (status == 1):
		return "RspClNoSession;Client Rejected, invalid session id"
	elif (status == 2):
                return "RspNeNoCalls;SRM unable to accept new calls"
	elif (status == 3):
                return "RspNeInvalidClient;SRM Rejected invalid clientId"
	elif (status == 4):
                return "RspNeInvalidServer;SRM Rejected invalid server Id"
	elif (status == 5):
                return "RspNeNoSession;SRM Rejected invalid session id"
	elif (status == 6):
                return "RspSeNoCalls;Server unable to accept new calls or NAG check failed"
	elif (status == 7):
                return "RspSeInvalidClient;Server rejected invalid client id"
	elif (status == 8):
                return "RspSeNoService;Server rejected Service Not available"
	elif (status == 16):
                return "RspSeNoSession;Server timed out, invalid sessionId"
	elif (status == 32):
                return "RspSeNoResource;Server unable to complete session setup owing to missing resource"
	elif (status == 36):
                return "RspSeProcError;Server detected error"
	elif (status == 39):
                return "RspSeFormatError;Server detected a format error."
	else :
		return "Session Setup Socket Connection Error"

def lscResponse(status):
	if(status == 0):
                return "LSC_OK;Success"
	elif(status == 16):
		return "Error code 0x10, LSC_BAD_REQUEST; Invalid request"
	elif(status == 17):
                return "Error code 0x11, LSC_BAD_STREAM; Invalid Stream handle"
	elif(status == 18):
                return "Error code 0x12, LSC_WRONG_STATE; Wrong State"
	elif(status == 19):
                return "Error code 0x13, LSC_UNKNOWN; Unknown Error"
	elif(status == 20):
                return "Error code 0x14,LSC_NO_PERMISSION; Client does not have permission for request"
	elif(status == 21):
                return "Error code 0x15,LSC_BAD_PARAM; Invalid parameter"
	elif(status == 22):
                return "Error code 0x16,LSC_NO_IMPLEMENT; Not implemented"
	elif(status == 23):
                return "Error code 0x17,LSC_NO_MEMORY; Dynamic memory allocation failure"
	elif(status == 24):
                return "Error code 0x18,LSC_IMP_LIMIT; Implementation Limit exceeded"
	elif(status == 25):
                return "Error code 0x19,LSC_TRANSIENT; Transient Error - reissue"
	elif(status == 26):
                return "Error code 0x1A,LSC_NO_RESOURCES; No resources"
	elif(status == 32):
                return "Error code 0x20,LSC_SERVER_ERROR; Server error"
	elif(status == 33):
                return "Error code 0x21,LSC_SERVER_FAILURE; Server has failed"
	elif(status == 48):
                return "Error code 0x30,LSC_BAD_SCALE; Incorrect Scale Value"
	elif(status == 49):
                return "Error code 0x31,LSC_BAD_START; Stream Start time does not exist"
	elif(status == 50):
                return "Error code 0x32,LSC_BAD_STOP; Stream Stop time does not exist"
	elif(status == 64):
                return "Error code 0x40,LSC_MPEG_DELIVERY; Unable to deliver MPEG stream"
	else :
		return "Error code not defined, could be socket error"
