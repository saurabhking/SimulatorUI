# This is to combine the error report files


import os

import csv
import os.path

errFlag = 0
statFlag = 0
if(os.path.isfile("healthchk/ctec-ndc1-proxy.csv")):
        source1 = csv.reader(open("healthchk/ctec-ndc1-proxy.csv","rb"))

if(os.path.isfile("healthchk/ctec-ndc2-proxy.csv")):
        source2 = csv.reader(open("healthchk/ctec-ndc2-proxy.csv","rb"))

if(os.path.isfile("healthchk/ctec-ndc3-proxy.csv")):
        source3 = csv.reader(open("healthchk/ctec-ndc3-proxy.csv","rb"))

dest = csv.writer(open("healthchk/healthchk-error-generr.csv","wb"))

errFile = open("healthchk/errorFound.txt","w")

def addtoerrorcsv(source,env):
	errFlag = 0
	count = 0
	counterr = 0
	flag = 0
	prevItem = None
	pacount = 0 
	for errchk in source:
	        result=errchk
        	for item in result:
			if((prevItem == "ProcessAlerts")and(flag == 1)):
				print "Here"
				print str(item)
				print result
				pacount = pacount + 1		 
				if(pacount > 1) :
	                                dest.writerow(result)
			if( item == "Connectivity Tests") or (item == "ProcessAlerts"):
				flag = 1
				prevItem = item 
			if((item != "Get Account Info")and(counterr ==1) and (flag == 1) and (prevItem == "Connectivity Tests")):
				if(item != ''):
					count = count + 1
			if (item == "Get Account Info"):
				flag = 0
				if(count > 0):
					list_str = "Connectivity requests to " + str(count) + " host failed"
					conn_list = ["Connectivity Test", "FAIL", list_str]		
					dest.writerow(conn_list)
                	if(item == "FAIL"):
				errFlag = 1
				addtoerrorcsv.counter += 1
				if((addtoerrorcsv.counter == 1)):
					dest.writerow(env)				
					global statFlag 
					statFlag = 1
				if (flag != 1):
				        dest.writerow(result)
		                        print result
	        		        print " "
				else:
					counterr = 1

	addtoerrorcsv.counter = 0
	if(errFlag == 0):
			env.append('PASS')
			dest.writerow(env)
addtoerrorcsv.counter = 0 
	
dest.writerow(" ")
dest.writerow(['Healthcheck Report MDMS-NDC1'])
dest.writerow(" ")
if(os.path.isfile("healthchk/ctec-ndc1-proxy.csv")):
        if(os.stat("healthchk/ctec-ndc1-proxy.csv").st_size != 0):
                src  = source1
		env = ['Proxy']
                addtoerrorcsv(src,env)



if(os.path.isfile("mdms_healthchk/healthchk_fsm/healthchk_fsm.csv")):
        if(os.stat("mdms_healthchk/healthchk_fsm/healthchk_fsm.csv").st_size != 0):
                src  = source5
                env = ['MDMS-FSM-IGUIDE']
                addtoerrorcsv(src,env)

if(os.path.isfile("mdms_healthchk/healthchk_fsm_spectrum/healthchk-FSM-Spectrum.csv")):
	if(os.stat("mdms_healthchk/healthchk_fsm_spectrum/healthchk-FSM-Spectrum.csv").st_size != 0):
                src  = source6
                env = ['MDMS-FSM-SPECTRUM']
                addtoerrorcsv(src,env)

if(os.path.isfile("mdms_healthchk/FSM_API_Response.csv")):
        if(os.stat("mdms_healthchk/FSM_API_Response.csv").st_size != 0):
                src  = source9
                env = ['FSM API TESTS']
                addtoerrorcsv(src,env)

dest.writerow(" ")
dest.writerow(" ")
dest.writerow(['Healthcheck Report MDMS-NDC2'])
dest.writerow(" ")
if(os.path.isfile("healthchk/ctec-ndc2-proxy.csv")):
        if(os.stat("healthchk/ctec-ndc2-proxy.csv").st_size != 0):
                src  = source2
		env = ['Proxy']
                addtoerrorcsv(src,env)



if(os.path.isfile("mdms_healthchk_ndc2/healthchk_fsm/healthchk_fsm.csv")):
        if(os.stat("mdms_healthchk_ndc2/healthchk_fsm/healthchk_fsm.csv").st_size != 0):
                src  = source7
                env = ['MDMS-FSM-IGUIDE']
                addtoerrorcsv(src,env)

if(os.path.isfile("mdms_healthchk_ndc2/healthchk_fsm_spectrum/healthchk-FSM-Spectrum.csv")):
        if(os.stat("mdms_healthchk_ndc2/healthchk_fsm_spectrum/healthchk-FSM-Spectrum.csv").st_size != 0):
                src  = source8
                env = ['MDMS-FSM-SPECTRUM']
                addtoerrorcsv(src,env)

dest.writerow(" ")
dest.writerow(" ")
dest.writerow(['Healthcheck Report MDMS-NDC3'])
dest.writerow(" ")
if(os.path.isfile("healthchk/ctec-ndc3-proxy.csv")):
        if(os.stat("healthchk/ctec-ndc3-proxy.csv").st_size != 0):
                src  = source3
		env = ['Proxy']
		print "ndc3"
                addtoerrorcsv(src,env)



dest.writerow(" ")
dest.writerow(" ")
dest.writerow(['Healthcheck Report MDMS-NDC4'])
dest.writerow(" ")
if(os.path.isfile("healthchk/ctec-ndc4-proxy.csv")):
        if(os.stat("healthchk/ctec-ndc4-proxy.csv").st_size != 0):
                src  = source4
		env = ['Proxy']
		print "ndc4"
                addtoerrorcsv(src,env)




if(statFlag == 1):
        errFile.write("Error Found")
else:
        errFile.write("No Error")
errFile.close()


