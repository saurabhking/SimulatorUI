from _lib import  *
from threading import Thread, Lock
import Queue
import time
import datetime
import settings
import os.path
import os
import xml.dom.minidom as m
from xml.dom.minidom import getDOMImplementation

log_obj=run_remote_command.log()
#session_id : takes session id as parameter; session_is is globale variable & can be refered in setting.py
#message_type: it can ssp, lsc, teardown; this variable is used by write_xml_logs to append logs/status/code to appropriate messages type
def write_xml_logs(session_id,message_type):
    try:
        xml_file_name="_logs/"+str(session_id+"_TestResultDetails")+".xml"
	#creating _log directory in case it does not exist
        if not(os.path.exists("_logs")):
            os.makedirs("_logs")

        if (os.path.isfile(xml_file_name)):
            newLog = m.parse(xml_file_name)
	    #Retrieving root xml  file tag
            SessionDetails_element = newLog.getElementsByTagName("SessionDetails").item(0)

        else:
            impl = getDOMImplementation()
            newLog = impl.createDocument(None, "SessionDetails", None)
            SessionDetails_element = newLog.documentElement
	    #creating root tag for xml file
            element_session = newLog.createElement("Session_ID")
            text_session=newLog.createTextNode(str(session_id))
            SessionDetails_element.appendChild(element_session)
            element_session.appendChild(text_session)

        element_step=newLog.createElement("testStep")
        SessionDetails_element.appendChild(element_step)

        element_step_name=newLog.createElement("Name")
        element_step.appendChild(element_step_name)
        text_msg_type=newLog.createTextNode(message_type)
        element_step_name.appendChild(text_msg_type)

	#setting variable name based on message type so that apprpriate global variable value could be retrieved
	if not "LSC" in str(message_type):
	    message_reponse=str(message_type)+"_status_code"
            message_status=str(message_type)+"_status"
        else:
            message_status="LSC_status"
	    message_reponse="LSC_status"
        if not "LSC" in str(message_type):
            
            if (getattr(settings,message_status)==True):
                element_msg_status=newLog.createElement("Result")
                element_step.appendChild(element_msg_status)

                text_msg_status=newLog.createTextNode("PASS")
                element_msg_status.appendChild(text_msg_status)

            else:
                element_msg_status=newLog.createElement("Result")
                element_step.appendChild(element_msg_status)

                text_msg_status=newLog.createTextNode("FAIL")
                element_msg_status.appendChild(text_msg_status)
	    
        else:
            if (int(str(getattr(settings,message_status)),16)==0):
                element_msg_status=newLog.createElement("Result")
                element_step.appendChild(element_msg_status)

                text_msg_status=newLog.createTextNode("PASS")
                element_msg_status.appendChild(text_msg_status)

            else:
                element_msg_status=newLog.createElement("Result")
                element_step.appendChild(element_msg_status)

                text_msg_status=newLog.createTextNode("FAIL")
                element_msg_status.appendChild(text_msg_status)	
	    try:
		text_LSC_OPCODE=newLog.createTextNode(str(settings.LSC_OPCODE))	    
		text_LSC_PLAY_SCALE=newLog.createTextNode(str(settings.LSC_SCALE_NUM))
		text_LSC_CNPT=newLog.createTextNode(str(settings.LSC_CNPT))
	    except:
		text_LSC_OPCODE=newLog.createTextNode(" ")
		text_LSC_PLAY_SCALE=newLog.createTextNode(" ")
		text_LSC_CNPT=newLog.createTextNode(" ")
	    element_LSC_OPCODE=newLog.createElement("LSC_OPCODE")
	    element_step.appendChild(element_LSC_OPCODE)
            #text_LSC_OPCODE=newLog.createTextNode(str(settings.LSC_OPCODE))
            element_LSC_OPCODE.appendChild(text_LSC_OPCODE)

	    element_LSC_PLAY_SCALE=newLog.createElement("LSC_PLAY_SCALE")
            element_step.appendChild(element_LSC_PLAY_SCALE)
            #text_LSC_PLAY_SCALE=newLog.createTextNode(str(settings.LSC_SCALE_NUM))
            element_LSC_PLAY_SCALE.appendChild(text_LSC_PLAY_SCALE)
		
            element_LSC_CNPT=newLog.createElement("LSC_CNPT")
	    element_step.appendChild(element_LSC_CNPT)
            #text_LSC_CNPT=newLog.createTextNode(str(settings.LSC_CNPT))
            element_LSC_CNPT.appendChild(text_LSC_CNPT)

        
	if(("SETUP" in str(message_type))  or ("LSC" in str(message_type))):
            element_code_details=newLog.createElement("Response_Details")
            element_step.appendChild(element_code_details)
            
            element_Summary=newLog.createElement("Summary")
            element_code_details.appendChild(element_Summary)
            element_Definition=newLog.createElement("Definition")
            element_code_details.appendChild(element_Definition)

            #response_details=(log_obj.response_details(message_type,getattr(settings,message_reponse))).split(";")
	    try:
                response=int(getattr(settings,message_reponse))
            except:
                response=str(getattr(settings,message_reponse))
	    #print ("*****")
	    #print response
	    #print message_type
	    try:
		response_details_data=(log_obj.response_details(message_type,response))
		response_details=response_details_data.split(";")
		text_Summary=newLog.createTextNode(response_details[0])
		text_Definition=newLog.createTextNode(response_details[1])
	    except:
                text_Summary=newLog.createTextNode("Invalid response received")
                text_Definition=newLog.createTextNode("")
            #response_details_data=(log_obj.response_details(message_type,response))
	    #print response_details_data
	    #response_details=response_details_data.split(";")
                                                    
            #text_Summary=newLog.createTextNode(response_details[0])
            element_Summary.appendChild(text_Summary)
            #text_Definition=newLog.createTextNode(response_details[1])
            element_Definition.appendChild(text_Definition)

  
	#element_log=newLog.createElement("log")
        #element_step.appendChild(element_log)
	#below try catch block retrieves all values from queue qu & appends them to xml file
        #try:
            #while True:
               #log_line=common_resource.qu.get(True,10)
               # element_line=newLog.createElement("line")
               # text_line=newLog.createTextNode(str(log_line))

                #element_log.appendChild(element_line)

                #element_line.appendChild(text_line)

                #common_resource.qu.task_done()
            #common_resource.qu.join()
        #except Exception as e:
            #print e
	lock=Lock()
	lock.acquire()
        newLog.writexml(open(xml_file_name,"w"))
	lock.release()
    except Exception as e:
	print "validation.py terminated with below exception ..."
        print e

#get_log_last_line_number is obsolete
def get_log_last_line_number(core_processing_no):
    try:
        ip=str(core_processing_no)+":IP"
	username=str(core_processing_no)+":username"
	pword=str(core_processing_no)+":password"
	command=str(core_processing_no)+":get_last_line_no"
	last_line_no=log_obj.run_command(ip,username,pword,command)		
        #print "Last line number in Log file is "
        #print last_line_no
        return last_line_no
    except Exception as e:
        print e
#get_logs_and_validate_old is obsolete			
def get_logs_and_validate_old(line_no,core_processing_no,message_type):
    #print line_no
    #time.sleep(40)
    try:
	global_variable=message_type+"_status"
	#st=getattr(settings,global_variable)
	#print st
	#print "global variable status"
	#print settings.global_variable
	#setattr(settings,global_variable, False)
	#settings.global_variable=False
	#st=getattr(settings,global_variable)
	#print st
	#print settings.global_variable
        last_line_no=str(line_no)
        #Defining  Thread
	command=str(core_processing_no)+":command"
	#updated_command=command.replace("last_log_line_no",last_line_no)
	ip=str(core_processing_no)+":IP"
	username=str(core_processing_no)+":username"
	pword=str(core_processing_no)+":password"		
        log=Thread(target=log_obj.run_command,args=(ip,username,pword,command,last_line_no,True,message_type,settings.SessionID,))
        log.setDaemon(True)
        log.start()
        log.join()
        write_xml_logs(settings.SessionID,message_type)
		
    except Exception as e:
        print e
#message_type: can be ssp, lsc , teardown
#elastic_search_server: it contains the url of elastic search server to collect logs; it uses default value in case user doesn't pass any value in main.py
def get_logs_and_validate(message_type,elastic_search_server="https://search-engprodtesting-xz4k4fabwqaawixv3cfl4nenle.us-east-1.es.amazonaws.com"):
    #time.sleep(40)
    try:
        global_variable=message_type+"_status"
	#seprate independent thread is created for each message type which retrieves & filters logs by using methods written _lib/run_remote_command.log/run_command
        #log=Thread(target=log_obj.run_command,args=(message_type,elastic_search_server,settings.SessionID,))
        #log.setDaemon(True)
        #log.start()
        #log.join()
	#write_xml_logs is called to append the values stored in queue qu  by above thread
        write_xml_logs(settings.SessionID,message_type)

    except Exception as e:
        print e

