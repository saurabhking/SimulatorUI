var express = require('express');
var path    = require("path");
var bodyParser = require('body-parser')
var fs = require('fs');
var http = require('http');
var app = express();
var readline = require('readline');
// Define to JSON type
//var property = JSON.parse(fs.readFileSync("properties.json"));
var config = require('./properties');
var template_file_location = config.config.template_file_location;
var macaddress_file_location = config.config.macaddress_file_location;
var asset_file_location = config.config.asset_file_location;
var report_file_location = config.config.report_file_location;
// prepare the header
var postheaders = {
    'Content-Type' : 'application/x-www-form-urlencoded'
};
var options = {
  host: config.config.avnapp_host,
  port: config.config.avnapp_port,
  path: '',
  method: '',
  headers : postheaders
};
// New call to compress content
//app.use(express.compress());
app.use( bodyParser.json() ); 
app.use(express.static(__dirname + '/Resources'));
app.get('/',function(req,res){   
	 res.sendFile(path.join(__dirname+'/index.html'));
});
app.get('/main',function(req,res){   
	 res.sendFile(path.join(__dirname+'/main.html'));
});
app.get('/stats',function(req,res){   
	 res.sendFile(path.join(__dirname+'/stats.html'));
});
app.get('/report',function(req,res){   
	 res.sendFile(path.join(__dirname+'/report.html'));
});
app.post('/startBatch', function (req, res) {
		var responseBody = '';
		try{
			console.log(req.body);
			var requestBody = req.body;
			requestBody.data.mac_file = macaddress_file_location+'/'+req.body.data.mac_file;
			requestBody.data.asset_file = asset_file_location+'/'+req.body.data.asset_file;
			
			requestBody.batch_parameters.process_lscp = config.config.process_lscp;
			requestBody.system={};
			//requestBody.system.id = config.config.headend;
			requestBody.system.id = req.body.data.headend;
			requestBody.system.version = config.config.system_version;
			requestBody.system.protocol = config.config.system_protocol;
			
			options.method='POST';
			options.path=config.config.url_create_job;
			//options.data=req.body;
						
			var reqPost = http.request(options, function(response) {
				response.on('data', function(chunk) {
					responseBody += chunk;
					console.log('in startBatch data Block');
					console.log(JSON.stringify(responseBody));
					res.end(JSON.stringify(JSON.parse(responseBody)));
						 });	 
				console.log('STATUS: ' + response.statusCode);
				//res.end(JSON.stringify(responseBody));
			}); 
			console.log(JSON.stringify(requestBody));
			reqPost.write(JSON.stringify(requestBody));
			reqPost.end();
			reqPost.on('error', function(e) {
				console.log('in startBatch error Block');
				console.error(e);
				res.end(JSON.stringify(responseBody));
			});
		}catch(e){
		console.log('in startBatch catch Block');
		console.log(e);
		res.end(JSON.stringify(responseBody));
		}
		
   });
   
app.get('/showBatch/:batchID', function (req, res) {
		var responseBody = '';
		try{
			console.log('batchID: '+req.params.batchID);
			if(req.params.batchID!='' && typeof req.params.batchID != 'undefined'){
				options.method='GET';
				options.path=config.config.url_show_job+req.params.batchID;
				var reqPost = http.request(options, function(response) {
					 response.on('data', function(chunk) {
							responseBody += chunk;
							console.log('in showBatch data');
							res.end(JSON.stringify(JSON.parse(responseBody)));
							});
					console.log('STATUS: ' + response.statusCode);
				});
				reqPost.end();
				reqPost.on('error', function(e) {
					console.log('in showBatch error Block');
					console.error(e);
					res.end(JSON.stringify(responseBody));
				});
			}else{
				res.end( JSON.stringify(responseBody));
			}
			}catch(e){
			console.log('in showBatch catch Block');
			console.log(e);
			res.end(JSON.stringify(responseBody));
		}
   });

app.post('/stopBatch/:batchID',function(req,res){
var responseBody='';
	try{
		console.log('batchID: '+req.params.batchID);
		if(req.params.batchID!='' && typeof req.params.batchID != 'undefined'){
			options.method='DELETE';
			options.path=config.config.url_stop_job+req.params.batchID;
			resData='';
			var reqPost = http.request(options, function(response) {
							response.on('data', function(chunk) {
							responseBody += chunk;
							console.log('in stopBatch data');
							res.end(JSON.stringify(JSON.parse(responseBody)));
					});
					console.log('STATUS: ' + response.statusCode);
					});
			  reqPost.end();
			  reqPost.on('error', function(e) {
						console.log('in stopBatch error Block');
						console.error(e);
						res.end(JSON.stringify(responseBody));
					});
		}else{
			res.end( JSON.stringify(responseBody));
			}
		}catch(e){
			console.log('in stopBatch catch Block');
			console.log(e);
			res.end(JSON.stringify(responseBody));
		}
}); 

app.get('/status',function(req,res){
var responseBody='';
	try{
		options.method='GET';
		options.path=config.config.url_engine_status;
		resData='';
		var reqPost = http.request(options, function(response) {
						response.on('data', function(chunk) {
						responseBody += chunk;
						console.log('in status of Load Engine data');
						res.end(JSON.stringify(JSON.parse(responseBody)));
				});
				console.log('STATUS: ' + response.statusCode);
				});
		  reqPost.end();
		  reqPost.on('error', function(e) {
					console.log('in status of Load Engine error Block');
					console.error(e);
					res.end(JSON.stringify(responseBody));
				});
		
		}catch(e){
			console.log('in status of Load Engine catch Block');
			console.log(e);
			res.end(JSON.stringify(responseBody));
		}
});   
   
app.get('/getFiles',function(req,res){
try{
	var template_files   = fs.readdirSync(template_file_location);
	var macaddress_files   = fs.readdirSync(macaddress_file_location);
	var asset_files   = fs.readdirSync(asset_file_location);
	fileList=JSON.parse('{"template":'+JSON.stringify(template_files)+',"mac":'+JSON.stringify(macaddress_files)+',"asset":'+JSON.stringify(asset_files)+',"avn":'+JSON.stringify(config.config.avn_gateway)+',"headend":'+JSON.stringify(config.config.headend)+'}');
	console.log(fileList);
	res.end( JSON.stringify(fileList));
	}catch(e){
		console.log(e);
		}
});

app.post('/saveTemplate',function(req,res){
try{
	var fileName='';
	if(req.body.fileName!='' && typeof req.body.fileName != 'undefined'){
		console.log('save file name with user given name : '+req.body.fileName);
		fileName = req.body.fileName;
	}else{
		console.log('save file name with date');
		fileName = getFileName();
	}
	req.body.batch_parameters.process_lscp = config.config.process_lscp;
	req.body.system={};
	//req.body.system.id = config.config.headend;
	req.body.system.id = req.body.data.headend;
	req.body.system.version = config.config.system_version;
	req.body.system.protocol = config.config.system_protocol;
	
	fs.writeFile(template_file_location+'/'+fileName+'.tmpl', JSON.stringify(req.body), function(err) {
    if(err) {
        return console.log(err);
    }
    console.log("The file was saved!");
	});
	res.end( JSON.stringify("success"));
	}catch(e){
		console.log(e);
		}
});

app.get('/loadTemplate',function(req,res){
try{
	resData = JSON.parse(fs.readFileSync(template_file_location+'/'+req.query.config, 'utf8'));
	console.log(resData);
	res.end( JSON.stringify(resData));
	}catch(e){
		console.log(e);
		}
});

app.get('/fetchReport',function(req,res){
try{
	var report = [];
	var todaysFile = report_file_location+'/session_info_'+getDate(0);
	var yesterdaysFile = report_file_location+'/session_info_'+getDate(1);
	
	if(fs.existsSync(todaysFile)){
		var rl = readline.createInterface({
		  input: fs.createReadStream(todaysFile)
		});
		rl.on('line', function (line) {
		  report.push(JSON.parse(line));  
		});
		rl.on('close',function(){
		if(fs.existsSync(yesterdaysFile)){
				var rl = readline.createInterface({
				  input: fs.createReadStream(yesterdaysFile)
				});
				rl.on('line', function (line) {
				  report.push(JSON.parse(line));  
				});
				rl.on('close',function(){
					res.end( JSON.stringify(report));
				});
				}else{
					res.end( JSON.stringify(report));
				}
			});
	}else if(fs.existsSync(yesterdaysFile)){
				var rl = readline.createInterface({
				  input: fs.createReadStream(yesterdaysFile)
				});
				rl.on('line', function (line) {
				  report.push(JSON.parse(line));  
				});
				rl.on('close',function(){
					res.end( JSON.stringify(report));
				});
	}else{
		res.end( JSON.stringify(report));
	}
}catch(e){
	console.log(e);
	res.end( JSON.stringify(report));
	}
});

function getDate(diff){

    var date = new Date();

    var year = date.getFullYear();

    var month = date.getMonth() + 1;
    month = (month < 10 ? "0" : "") + month;

    var day  = date.getDate();
	day = day-diff;
    day = (day < 10 ? "0" : "") + day;

    return year + "" +month + "" + day;

}

function getFileName() {

    var date = new Date();

    var hour = date.getHours();
    hour = (hour < 10 ? "0" : "") + hour;

    var min  = date.getMinutes();
    min = (min < 10 ? "0" : "") + min;

    var sec  = date.getSeconds();
    sec = (sec < 10 ? "0" : "") + sec;

    var year = date.getFullYear();

    var month = date.getMonth() + 1;
    month = (month < 10 ? "0" : "") + month;

    var day  = date.getDate();
    day = (day < 10 ? "0" : "") + day;

    return year + "-" + month + "-" + day + "-" + hour + "-" + min + "-" + sec;

}

process.on('uncaughtException', function(err) {
  console.log('Caught uncaughtException: ' + err);
});

//--------------------------------------------------MOCK START-----------------------------------------------------

app.post('/1/create/newJob',function(req,res){
	console.log('mock to create new job :' + req.body);
	res.end( JSON.stringify({"info" : {"batchID" : "0123456789","start_time"  : "12:00:00","sessions_count" : "123"}}));
});
app.get('/1/status/job',function(req,res){
	console.log('mock to get batch status : '+req.params.batchId);
	res.end( JSON.stringify({"status" : "running","info" : {"sessions_creating" : "123","sessions_created"  : "123","sessions_existing" : "123","sessions_tearing" : "123","sessions_torn" : "123","sessions_torn_by_server" : "123","sessions_create_failed" : "123","average_setup_time" : "123","average_release_time" : "123"}}));
});
app.delete('/1/stop/:batchId',function(req,res){
	console.log('mock to stop batch : '+req.params.batchId);
	res.end( JSON.stringify({"info" : {"batchID" : "0123456789","start_time"  : "12:00:00","sessions_count" : "123",}}));
});
//--------------------------------------------------MOCK END--------------------------------------------------------

app.listen(process.env.PORT || config.config.port);
console.log("Running at Port "+config.config.port);
