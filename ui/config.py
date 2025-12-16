#mode = 'fsm or proxy'
mode='fsm'
headend='ctec_a3h2'
digitalsmith_base_url='http://charter-staging-elb.digitalsmiths.net/sd/charter/cores/assets-charter/search?q=*:*&schedule.q=*type:VOD headendId:('+headend+') titleAssetId:'
mdms_url="http://71.85.81.215:8300"
#in case of proxy mode
mongo_uri="mongodb://admin:admin1234@172.30.111.27:27017/?authMechanism=SCRAM-SHA-1"
def get_host(headend_name):
	if(headend_name == "ctec_a3h2"):
		return "mdms-int01-dsmcc-ndc.sa.g.charterlab.com","172.30.84.137","mdms-int01-settings-ndc.sa.g.charterlab.com"
	if(headend_name == "BC5"):
		return "mdms-int01-dsmcc-ndc.sa.g.charterlab.com","172.16.146.166","mdms-int01-settings-ndc.sa.g.charterlab.com"
