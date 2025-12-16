# Guide to use the script's package for Session Setup Simulator

Scripts Included :- 

1.) main.py :- This is the main script which will call all the other script in order to formulate the messages and sending the message 
	       viz. Session Setup, HeartBeat, Teardown, LSC_PLAY, LSC_PAUSE, LSC_FWD, LSC_RWD & LSC_STATUS to the required server
	       for the VOD session simulation. 

2.) settings.py :- This is a placeholder for the global variable's which are used among the files, especially mainly SessionID.
		   It also creates the SessionID from MAC & and a random session number.  

3.) sessfrm.py :- This script formulates the Session setup message from the Assetname passed from UI. 

4.) hbform.py :- This script formulates the HeartBeat message. 

5.) tearform.py :- This script formulates the Teardown message. 

6.) lscform.py :- This script forms the LSC_PLAY, PAUSE, FWD, RWD & STATUS message and pass them to LSCP Server 2. 

7.) titleList.py :- This script fetches the Asset List from MongoDB. 


Usage :- 

sudo main.py '<mac>' '<AssetName>'

