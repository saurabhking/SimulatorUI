myApp.controller('MainCtrl', function($scope, $routeParams,$location, myFactory) {
		
    $scope.reset = function() {
        $scope.user = {};
		//$scope.user.system={};
		$scope.user.data={};
		$scope.user.batch_parameters={};
		//$scope.user.batch_parameters.process_lscp='false';
		$scope.user.avn={};
		//$scope.user.system.id = 'st_louis';
		//$scope.user.system.version = '00';
		//$scope.user.system.protocol = '01';
		myFactory.populatePage($scope);
    }; 
	$scope.reset();

	$scope.startBatch = function() {
	try{
	
		myFactory.getStatus(function(data){
		console.log(data);
		$scope.engine_status=data.status;
		if ($scope.engine_status == 'Idle'){
			var ipHost =  $scope.user.avn.avn_gw_host.split(":");
			$scope.user.avn.avn_gw_host = ipHost[0];
			$scope.user.avn.avn_gw_port	= Number(ipHost[1]);
			console.log($scope.user);
			myFactory.startBatch($scope,function(data){
			if(data['error']){
				$scope.mainError = data.error;
				$scope.user.avn.avn_gw_host = ipHost[0]+':'+ipHost[1];
			}else{
				console.log('start batch : '+data);
				myFactory.setbatch(data.info.batchID);
				console.log('batch numer --------------------->'+data.info.batchID);
				$location.path('/stats');
			}
			});
		}else{
			$scope.mainError = 'Load Engine is  active, processing Batch '+data.info[0].batch_id;
		}
		});
		
		}catch(e){
			console.log(e);
		}
   };
	
	$scope.loadTemplate = function() {
	try{
			myFactory.loadTemplate($scope,function(data){	
				console.log(data);
				//$scope.user.system.id = data.system.id;
				//$scope.user.system.version = data.system.version;
				//$scope.user.system.protocol = data.system.protocol;				
				$scope.user.data.asset_file = data.data.asset_file;
				$scope.user.data.mac_file =  data.data.mac_file;
				$scope.user.data.headend =  data.system.id;
				$scope.user.avn.avn_gw_host = data.avn.avn_gw_host+':'+data.avn.avn_gw_port;
				$scope.user.batch_parameters.session_duration = data.batch_parameters.session_duration;
				$scope.user.batch_parameters.creation_period = data.batch_parameters.creation_period;
				$scope.user.batch_parameters.creation_rate = data.batch_parameters.creation_rate;
				
		});
      }catch(e){
		console.log(e);
		}         
    };
	
  $scope.saveTemplate = function (){
  
	$scope.user.fileName = prompt("Enter File name : ", "");

	try{
		var ipHost =  $scope.user.avn.avn_gw_host.split(":");
		$scope.user.avn.avn_gw_host = ipHost[0];
		$scope.user.avn.avn_gw_port	= Number(ipHost[1]);
		console.log($scope.user);
		myFactory.saveTemplate($scope,function(response){
				console.log(response);
				$scope.user.avn.avn_gw_host = ipHost[0]+':'+ipHost[1];
				},function(error){	
				$scope.user.avn.avn_gw_host = ipHost[0]+':'+ipHost[1];
				console.log('Fail');
				});
		}catch(e){
		console.log(e);
		}
  };
	
});
myApp.controller('StatsCtrl', function($scope, $interval,$location, myFactory) {

	$scope.populate = function(){
		batch = myFactory.getbatch();
		console.log(batch);
		if(batch!='' && !(typeof batch === 'undefined')){
		console.log('here in populate stats');
			$scope.batchID = batch ;
			if($scope.batchID != ''){
			myFactory.showBatch($scope,function(response){
							console.log(response);
							populateFields(response);
						},function(error){
						console.log('Fail');
						$scope.statsError ='Fail to get Batch';						
						});
				}
		}
	}	
	
	$scope.back = function(){
		$scope.batchID = '' ;
		$location.path('/');
	}
	
	$scope.refresh = function(){
		console.log('refresh');
		myFactory.setbatch($scope.batchID);
		$scope.populate();
	}
	
	refreshTimer = $interval(function(){
		console.log('interval call');
		myFactory.setbatch($scope.batchID);
		$scope.populate();
	},5000);
	
	$scope.$on('$destroy', function() {
      $interval.cancel(refreshTimer);
    });
	
	$scope.stop = function(){
		if(confirm("Do you want to Stop this Batch!")){
			myFactory.stopBatch($scope,function(response){
			console.log(response);
				if(response['error']){
				$scope.statsError = response.error;
				}else{
				console.log('Success');
				}
			},function(error){		
				console.log('Fail');
				$scope.statsError ='Fail to Stop Batch';
			});
		}
	}
	
	function populateFields(data){
	console.log('response data :' + data);
		
		if(data['error']){
			$scope.statsError = data.error;
		}else{
		$scope.statsError ='';
		$scope.sessions_creating 	=	data.info.sessions_creating;
		$scope.sessions_torn_by_server 	=	data.info.sessions_torn_by_server;
		$scope.sessions_created 	=	data.info.sessions_created;
		$scope.sessions_create_failed 	=	data.info.sessions_create_failed;
		$scope.sessions_teardown_failed 	=	data.info.sessions_teardown_failed;
		$scope.sessions_existing 	=	data.info.sessions_existing; 
		$scope.average_setup_time  	=	data.info.average_setup_time.toFixed(2); 
		$scope.sessions_tearing 	=	data.info.sessions_tearing;
		$scope.average_release_time 	=	data.info.average_release_time.toFixed(2); 
		$scope.sessions_torn 	=	data.info.sessions_torn; 
		$scope.starttime 	=	data.start_time; 
		$scope.finishtime 	=	data.end_time;  
		}
					
	}
	$scope.populate();
});

myApp.controller('ReportCtrl', function($scope, $routeParams,$location, myFactory) {
	
	$scope.back = function(){
		$location.path('/');
	}
	
	
	myFactory.fetchReport($scope,function(response){
		console.log(response);
		$scope.report=response;
		},function(error){		
			console.log('fail');
			$scope.reportError ='Fail to Load Report.';
		});
	
	 $scope.predicate = 'start_time';
	$scope.reverse = false;
	
	$scope.order = function(predicate) {
    $scope.reverse = ($scope.predicate === predicate) ? !$scope.reverse : false;
    $scope.predicate = predicate;
  };
});