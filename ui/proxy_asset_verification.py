import os
import sys
import pymongo 
import requests
import config
from pymongo import MongoClient

assetList = []	

def digitalsmith_curl(assetId):
	digsmith1 = '&fl=relevantSchedules.*&limit=5&disableRemoveNonEnglish=true&includeAdult=false&facet=false&facet.field=title&facet.field=relevantSchedules.packageproviderid&facet.field=relevantSchedules.categories&facet.limit=5&facet.sort=value&enable.merchandising=false'
	dig_url = config.digitalsmith_base_url + assetId + digsmith1 
	payload = ""
	r = requests.get(dig_url, params=payload)
	j = r.json()
	if (j['hitCount'] > 0):
		try:
			title= j['hits'][0]['relevantSchedules'][0]['title']
			categories= j['hits'][0]['relevantSchedules'][0]['categories']
			return True , title , categories
		except:
			return False , '', ''	
	else:
		return False , '', ''


def assetInMDMS():
	uri = config.mongo_uri
	connection = MongoClient(uri)
	db = connection.ADAPTERDB
	document = db.openstream_offerings.find({'headendId':config.headend,'createTime': {"$gt": "2017-05-19T20:51:05Z"}},{'offeringId':1,"_id":0,'titleAsset.assetName':1})
	print('document count for assetID ----------------> ', document.count())
	for row in document:
		id = row["titleAsset"]["assetName"]
		assetId = id.split('::')[1]
		result = digitalsmith_curl(assetId)
		if(result[0]):
			print assetId,'::',result[1],'::',result[2]
			data = '<tr><td>'+assetId+'</td><td>'+str(result[1])+'</td><td>'+str(result[2])+'</td></tr>'
			assetList.append(data)


def run():
	global assetList
	assetInMDMS()
	htmlfile = open('my.html',"w")
	htmlfile.write('<table>')
	for asset in assetList:
		htmlfile.write(asset)
	htmlfile.write('</table>')
