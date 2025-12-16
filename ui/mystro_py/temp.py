import re
re1=open("_logs/000004e0b57f000ec7f1_TestResultDetails.xml")
x='action\,\"HEARTBEAT\"\}\,\{comp\_code\,\"OK\"'
#x='action,"HEARTBEAT"},{comp_code,"OK"'
for line in re1:
	
#    if r'x' in line:
    if re.match(r'x',line):
	print "found"
