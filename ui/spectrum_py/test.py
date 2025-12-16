import time 

#startDate = '2016-10-25T06:00:00Z'
startDate = '2016-11-01T06:00:00Z'
timePattern = '%Y-%m-%dT%H:%M:%SZ'
startTimeInt = int(time.mktime(time.strptime(startDate,timePattern )))
#print startTimeInt
startTime = str(startTimeInt)
print startTime
