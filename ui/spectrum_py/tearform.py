# This script will formulate the Teardown Message

import settings

def initTeardown():
	TEARSTR_HEADER = '11024020c7f0002aff000014'
	TEARSTR_USERDATA = '00000000000401000000'
	print("*********************************************************************************>",settings.SessionID)
	TEARDOWNSTR = TEARSTR_HEADER + settings.SessionID + TEARSTR_USERDATA
	return TEARDOWNSTR.decode('hex')


