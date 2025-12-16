import config
import fsm_asset_verification
import proxy_asset_verification

def getasset():
	asset = ''
	if(config.mode=='fsm'):
		#asset =fsm_asset_verification.run()
		asset = 'ctec_a3h2-sho.com-XPTL0001441106983001-1444024800000'
	if(config.mode=='proxy'):
		asset =proxy_asset_verification.run()
	return asset