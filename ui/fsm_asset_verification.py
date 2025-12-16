import os
import sys
import pymongo 
import requests
import commands
import config
from pymongo import MongoClient
from xml.etree import ElementTree

asset = ''

def digitalsmith_curl(assetId):
	digsmith1 = '&fl=relevantSchedules.*&limit=5&disableRemoveNonEnglish=true&includeAdult=false&facet=false&facet.field=title&facet.field=relevantSchedules.packageproviderid&facet.field=relevantSchedules.categories&facet.limit=5&facet.sort=value&enable.merchandising=false'
	dig_url = config.digitalsmith_base_url + assetId + digsmith1 
	payload = ""
	r = requests.get(dig_url, params=payload)
	j = r.json()
	if (j['hitCount'] > 0):
		try:
			content = j['hits'][0]['relevantSchedules'][0]['movieAsset']['Content']
			delivery_id= j['hits'][0]['relevantSchedules'][0]['id']
			result = commands.getoutput('curl -Is '+content+' | head -1')
			if('200 OK' in result):
				print("--------------------delivery_id found-------------------- ",delivery_id)
				return True , delivery_id
			else:
				return False , ''
		except:
			return False ,''
	else:
		return False ,''


def assetInMDMS(offset):
	global asset
	mdms_curl= config.mdms_url+"/assets?assetType=Title&details=full&offset="+str(offset)
	r = requests.get(mdms_curl)
	root = ElementTree.fromstring(r.content)
	size = len(root.getchildren())
	for child in root:
		id = child.get('uriId')
		assetId = id.split('/')[2]
		result = digitalsmith_curl(assetId)
		if(result[0]):
			asset = str(result[1])
			size=0
			break
	return size


def run():	
	offset = 0
	size = 1000
	while(size >= 1000):
		offset = offset + 1000
		size = assetInMDMS(offset)
	return asset
