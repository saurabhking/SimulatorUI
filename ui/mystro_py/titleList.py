# This Script is intended to generate the list of available title from openstream offerings.
import xml.etree.cElementTree as ET
import pymongo
from pymongo import MongoClient
from mako.template import Template
from mako.runtime import Context

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

tpl_xml = '''<?xml version="1.0" ?>
<AssetLists>
% for i in data:
<Asset>
<Title>${i[0]}</Title>
<OfferingId>${i[1]}</OfferingId>
</Asset>
% endfor
</AssetLists>
'''
uri = ''
import pymongo
from pymongo import MongoClient
# Function to get the primary db uri
def findPrimaryDb():
        global uri
        uri = "mongodb://admin:admin1234@172.16.146.84:27017/?authMechanism=SCRAM-SHA-1"
        print "Primary Mongo DB URI"
        print uri



def fetchList():
	titleList = []
	global uri
	#uri = "mongodb://admin:admin1234@192.168.194.241:27020"
	findPrimaryDb()
	connection = MongoClient(uri)
	db = connection.ADAPTERDB
	listquery = db.openstream_offerings.find({},{'description':1, 'offeringId':1,"_id":0,})
	for result in listquery:
		dbresult = result
		movieTitle  =str((dbresult['description']).encode('utf-8')) 
		offeringId = (dbresult['offeringId'])
		tup = (movieTitle,offeringId)
		global titleList
		titleList.append(tup)
	return titleList

titleList = fetchList()

titleLed=len(titleList)
AssetLists = ET.Element("AssetLists")
for i in range(0,titleLed):
    print titleList[i]
    Asset = ET.SubElement(AssetLists,"Asset")
    Title = ET.SubElement(Asset,"Title")
    OfferingId = ET.SubElement(Asset,"OfferingId")

    Title.text = str(titleList[i][0])
    OfferingId.text = str(titleList[i][1])

    tree = ET.ElementTree(AssetLists)
tree.write('SC1_AssetLists.xml')
'''
tpl = Template(tpl_xml)

with open('AssetLists.xml', 'w') as f:
    ctx = Context(f, data=titleList)
    tpl.render_context(ctx)
'''
