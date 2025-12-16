import paramiko
import ConfigParser
import os
import re
import time
#from common_resource import qu, start_time,pattern
from common_resource import qu, start_time
import settings
import ast

class log:
    def __init__(self):
	print "*****"
        pass
		
    def response_details(self,message_type,response_code):
        try:
	    if ("LSC" in str(message_type)):
		message_type="LSC"
            config_data=self.read_config_file("_config/config.cfg")            
	    code_dict=eval((config_data.get("STATUS_CODE",message_type).strip("'")))
	    print "******"
	    print message_type
	    print response_code
	    print code_dict[response_code]
            return code_dict[response_code]

        except Exception as e:
            print e
    def run_command_old(self,IP,uname,pword,command,last_line_no=None,validate_pattern=False,message_type=None,session_id=None):
        try:
            get_ip=IP.split(":")
	    #print get_ip
	    get_uname=uname.split(":")
	    get_pword=pword.split(":")
	    get_command=command.split(":")
	    #print get_command
	    config_data=self.read_config_file("_config/config.cfg")
	    IP=config_data.get(get_ip[0],get_ip[1])
	    #print IP
	    uname=config_data.get(get_uname[0],get_uname[1])
	    pword=config_data.get(get_pword[0],get_pword[1])
	    command=config_data.get(get_command[0],get_command[1])
	    #print command


            ssh=paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(IP, username=uname,password=pword)
            #stdin,stdout,stderr=ssh.exec_command(command)
            if (validate_pattern):
                pattern = []
		updated_command=command.replace("last_log_line_no",last_line_no)
		#print updated_command
                updated_command_1=updated_command+" | grep "+str(session_id)
                stdin,stdout,stderr=ssh.exec_command(updated_command_1)
                #config_data=self.read_config_file("_config/config.cfg")
                for data in config_data.options(message_type):
                    pattern_msg=config_data.get(message_type,data).strip('"')
                    pattern_with_session_id=pattern_msg.replace("session_id",str(session_id))
                    pattern.append(eval(pattern_with_session_id))
                    #print pattern_with_session_id

                index=0
                #print pattern[index]
                for line in  stdout.readlines():
                    #print line
		    qu.put(line)
                    match = re.search(pattern[index], line)
                    if match:
                        message_status=str(message_type)+"_status"
			if (("HEARTBEAT" in str(message_type)) and (re.search("comp_code\,\"OK\"", line))):
			    setattr(settings,message_status, True)
			    
                        #if re.search("comp_code\,\"OK\"", line):
                        #    setattr(settings,message_status, True)
                        #    #settings.SSP_status=True
                        #print line
                        #qu.put(line)
                        if (index == len(pattern) -1 ):
                            #qu.put("Message verification succeed")
                            #print "Message verification succeed"
                            #message_status=str(message_type)+"_status"
                            #settings.message_status=True
			    #if (("HEARTBEAT" in str(message_type)) or ("TEARDOWN" in str(message_type))):
			    if ("HEARTBEAT" in str(message_type)):
				print "setting status in lib"
				print message_status
				setattr(settings,message_status, True)
                            return
                        index=index+1
                return False
			
            stdin,stdout,stderr=ssh.exec_command(command)
            for line in  stdout.readlines():
                line_no=line.strip("\n")
                return line_no
            #return stdout.readlines()[0].strip("\n")


        except Exception as e:
            print e
    def run_command(self,message_type,elastic_search_server=None,session_id=None):
        try:
	    config_data=self.read_config_file("_config/config.cfg")
	    pattern = []
            for data in config_data.options(message_type):
		pattern_msg=config_data.get(message_type,data).strip('"')
                pattern_with_session_id=pattern_msg.replace("session_id",str(session_id))
		#print pattern_with_session_id
                pattern.append(eval(pattern_with_session_id))

            from elasticsearch import Elasticsearch
            es = Elasticsearch(elastic_search_server)
            res=es.search(q='message:'+str(session_id),sort= 'timestamp:asc', size = 700)

            index=0
            for hit in res['hits']['hits']:
                line=hit['_source']['message']
		#print line
                match = re.search(pattern[index], line)
		#print pattern[index]
		#print match
                x=r'\{action\,\"HEARTBEAT\"\}\,\{comp\_code\,\"OK\"\}'
                if match:
                    qu.put(line)
		    #print message_type
                    if (("HEARTBEAT" in str(message_type)) and (re.search(x,line))):
			message_status=str(message_type)+"_status"
                        setattr(settings,message_status, True)
                
                    if (index == len(pattern) -1 ):
                        return
                    index=index+1
	    return
            '''
            config_data=self.read_config_file("_config/config.cfg")

            import urllib2
            url = "http://"+str(elastic_search_server)+"/_search?q=message:"+str(session_id)
            req = urllib2.Request(url)
            stdout = urllib2.urlopen(req)

	    
            for data in config_data.options(message_type):
                    pattern_msg=config_data.get(message_type,data).strip('"')
                    pattern_with_session_id=pattern_msg.replace("session_id",str(session_id))
                    pattern.append(eval(pattern_with_session_id))            
	
	    
            for line in  stdout:
                print line
                qu.put(line)
		#x=r'action\,\"HEARTBEAT\"\}\,\{comp\_code\,\"OK\"'\{action\,\"HEARTBEAT\"\}\,\{comp\_code\,\"OK\"\}
		x=r'\{action\,\"HEARTBEAT\"\}\,\{comp\_code\,\"OK\"\}'
		#x=r'\,\"hits\"\:\{\"total\"'
		print re.search(x,line)
		if (("HEARTBEAT" in str(message_type)) and (r'x' in line)):
		#if re.search(x,line):
		    print "True"
		    message_status=str(message_type)+"_status"
		    setattr(settings,message_status, True)
            return
	    '''            
        except Exception as e:
            print e
    def read_config_file(self,conf_file):
        try:
            config=ConfigParser.ConfigParser()
            with open(conf_file,'r') as conf_file:
                config.readfp(conf_file)
            return config
        except Exception as e:
            print e

