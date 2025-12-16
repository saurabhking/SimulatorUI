#!/usr/bin/env python

'''
Created on July 27, 2017

@author: ssingh
'''
import os
import sys
import logging
import json
import thread
import config
import time
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify, abort, request, make_response
from datetime import datetime, timedelta
import argparse
import asset
sys.path.append(os.getcwd()+'/spectrum_py')
sys.path.append(os.getcwd()+'/mystro_py')
import mystro_main
import main_spectrum

LISTEN_DEFAULT = '127.0.0.1:5000'
CLI_ARGS = None
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route("/", methods = ['GET'])
def root():
    return app.send_static_file('index.html')

@app.route("/main", methods = ['GET'])
def main():
    return app.send_static_file('main.html')

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def custom_abort(code,error_message):
    abort( make_response(jsonify({"error": True, "error_message": error_message}), code))

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { "error": True, "error_message": "Bad request" } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { "error": True, "error_message": "Not Found"} ), 404)

@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify( { "error": True, "error_message": "Internal Error" } ), 500)

#@app.route('/', defaults={'path': ''})
#@app.route('/<path:path>')
#def catch_all(path):
#    custom_abort(400,'Bad Request')

@app.route('/session/start', methods = ['POST'])
def start():
	res= {"error": True}
	req = request.get_json()
	print(req)
	tsid = req['tsid']
	headend = req['headend']
	deliveryid = req['deliveryid']
	mac = req['mac']
	npt = req['npt']
	host = config.get_host(str(headend))
	thread.start_new_thread( main_spectrum.start, (str(host[0]),str(host[1]),str(mac),str(deliveryid),str(npt),str(headend),str(tsid)) )
	time.sleep(5)
	if(main_spectrum.active):
		res= {"error": False ,"sessionid":main_spectrum.sessionid}
	return jsonify( res )


@app.route('/session/play', methods = ['POST'])
def play():
	res= {"error": True}
	code  = main_spectrum.play()
	res= {"error": False,"code": code}
	return jsonify( res )	
	
@app.route('/session/pause', methods = ['POST'])
def pause():
	res= {"error": True}
	code  = main_spectrum.pause()
	res= {"error": False,"code": code}
	return jsonify( res )	
	
@app.route('/session/ff', methods = ['POST'])
def ff():
	res= {"error": True}
	code  = main_spectrum.ff()
	res= {"error": False,"code": code}
	return jsonify( res )

@app.route('/session/rw', methods = ['POST'])
def rw():
	res= {"error": True}
	code  = main_spectrum.rw()
	res= {"error": False,"code": code}
	return jsonify( res )

@app.route('/session/teardown', methods = ['POST'])
def teardown():
	res= {"error": False}
	print(request.data)
	main_spectrum.teardown()
	return jsonify( res )

@app.route('/session/asset', methods = ['GET'])
def fetch_asset():
	delivery_id = asset.getasset()
	res= {"id": delivery_id}
	return jsonify( res )

@app.route('/session/getaccount', methods = ['POST'])
def get_account():
	req = request.get_json()
	print(req)
	headend = req['headend']
	mac = req['mac']
	setting_api_host = config.get_host(str(headend))
	rentals = main_spectrum.get_account(mac,setting_api_host[2],str(headend))
	print (rentals)
	return jsonify(rentals)
	
if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Starts Session Setup server.')
    arg_parser.add_argument("--listen", type=str, default=LISTEN_DEFAULT, help = "host settings (default %s)" % (LISTEN_DEFAULT))
    arg_parser.add_argument("--debug", action="store_true", default=False, help = "Show tracebacks and auto reload")
    arg_parser.add_argument("--logdir", type=str, help = "Log directory to put all related log files")
    arg_parser.add_argument("-p", "--pidfile", nargs=1, metavar="PID_PATH", help="Path to PID file.")
    args = arg_parser.parse_args()
    CLI_ARGS = args
    host, port = args.listen.split(':')
    app.run(host=host,port=int(port),debug = CLI_ARGS.debug)
