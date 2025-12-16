# This Script is intended to generate the list of available title from openstream offerings.
import xml.etree.cElementTree as ET
import pymongo
from pymongo import MongoClient

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os


def fetchList(headendId):
	titleList = []
	uri = "mongodb://admin:admin1234@172.16.146.84:27017/?authMechanism=SCRAM-SHA-1"
	connection = MongoClient(uri)
	db = connection.ADAPTERDB
	listquery = db.openstream_offerings.find({'headendId':headendId},{'description':1, 'offeringId':1,"_id":0,})
	for result in listquery:
		dbresult = result
		movieTitle  =str((dbresult['description']).encode('utf-8')) 
		offeringId = (dbresult['offeringId'])
		tup = (movieTitle,offeringId)
		global titleList
		titleList.append(tup)
	return titleList
def Asset_detail(headend_id):
    if not(os.path.exists("_asset")):
	os.makedirs("_asset")
    titleList = fetchList(headend_id)
    titleLed=len(titleList)
    print titleLed
    AssetLists = ET.Element("AssetLists")
    for i in range(0,titleLed):
        #print titleList[i]
        Asset = ET.SubElement(AssetLists,"Asset")
        Title = ET.SubElement(Asset,"Title")
        OfferingId = ET.SubElement(Asset,"OfferingId")

        Title.text = str(titleList[i][0])
        OfferingId.text = str(titleList[i][1])

    tree = ET.ElementTree(AssetLists)
    asset_file="_asset/"+str(headend_id)+"_AssetLists.xml"
    tree.write(asset_file)
