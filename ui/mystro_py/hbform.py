# This Script formulates the HeartBeat Message

import settings

HB_HEADER = '110240b000000000ff00000c0001'
HEARTBEATSTR = HB_HEADER + settings.SessionID
HEARTBEAT = HEARTBEATSTR.decode('hex')
#print HEARTBEAT
