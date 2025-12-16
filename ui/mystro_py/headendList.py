# This Script is intended to generate the list of available title from openstream offerings.
import xml.etree.cElementTree as ET
import pymongo
from pymongo import MongoClient
import titleList_headend 
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def fetchList():
	siteList = []
	uri = "mongodb://admin:admin1234@172.16.146.84:27017/?authMechanism=SCRAM-SHA-1"
	connection = MongoClient(uri)
	db = connection.ADAPTERDB
	listquery = db.sites.find({},{'headendId':1,"_id":0})
	for result in listquery:
		dbresult = result
		site = (dbresult['headendId'])
		print site
		titleList_headend.Asset_detail(site)
		tup = (site)
		global siteList
		siteList.append(tup)
	return siteList

siteList = fetchList()
siteLed=len(siteList)
print siteLed
SiteList = ET.Element("SiteList")
for i in range(0,siteLed):
    print siteList[i]
    HeadendId = ET.SubElement(SiteList,"HeadendId")
    #Title = ET.SubElement(Asset,"Title")
    #OfferingId = ET.SubElement(Asset,"OfferingId")

    HeadendId.text = str(siteList[i])
    #OfferingId.text = str(titleList[i][1])

    tree = ET.ElementTree(SiteList)
    tree.write('HeadendLists.xml')


