myApp.controller('MainCtrl', function($scope, $routeParams,$location, myFactory) {
	
	$scope.headends = ['BC5','ctec_a3h2']
	$scope.templates = ['nothing','nothing']
	$scope.user = {}
	$scope.user.npt = "0"
	$scope.user.rentals = {}
	$scope.user.status = ""
	$scope.start = function (){
	try{
		myFactory.start($scope,function(response){
				console.log(response);
				$scope.user.sessionid = response.sessionid
				$scope.user.status = "SessionID = " +$scope.user.sessionid+ " is Start .\\n"
				$("#start").prop("disabled",true);
				},function(error){	
				console.log('Fail');
				});
		}catch(e){
		console.log(e);
		}
  };
  $scope.play = function (){
	try{
		myFactory.play($scope,function(response){
				console.log(response);
				$scope.user.status = $scope.user.status + "Press PLAY Button .\\n"
				},function(error){	
				console.log('Fail');
				});
		}catch(e){
		console.log(e);
		}
  };
  $scope.pause = function (){
	try{
		myFactory.pause($scope,function(response){
				console.log(response);
				$scope.user.status = $scope.user.status + "Press PAUSE Button .\\n"
				},function(error){	
				console.log('Fail');
				});
		}catch(e){
		console.log(e);
		}
  };
  	$scope.ff = function (){
	try{
		myFactory.ff($scope,function(response){
				console.log(response);
				$scope.user.status = $scope.user.status + "Press FAST FORWARD Button .\\n"
				},function(error){	
				console.log('Fail');
				});
		}catch(e){
		console.log(e);
		}
  };
  
  	$scope.rw = function (){
	try{
		myFactory.rw($scope,function(response){
				$scope.user.status = $scope.user.status + "Press REWIND Button .\\n"
				console.log(response);
				},function(error){	
				console.log('Fail');
				});
		}catch(e){
		console.log(e);
		}
  };
  
  $scope.teardown = function (){
	try{
		myFactory.teardown($scope,function(response){
				console.log(response);
				$scope.user.status = $scope.user.status +"SessionID : "+ $scope.user.sessionid +  " STOPPED .\\n"
				$("#start").prop("disabled",false);
				},function(error){	
				console.log('Fail');
				});
		}catch(e){
		console.log(e);
		}
  };	
  $scope.asset = function (){
	try{
		myFactory.asset($scope,function(response){
				console.log(response);
				$scope.user.deliveryid = response.id;
				},function(error){	
				console.log('Fail');
				});
		}catch(e){
		console.log(e);
		}
  };
  $scope.getaccount = function (){
	try{
		myFactory.getaccount($scope,function(response){
				console.log(response);
				$scope.user.rentals = response;
				},function(error){	
				console.log('Fail');
				});
		}catch(e){
		console.log(e);
		}
  };
  $scope.render_npt = function (){
		$scope.user.npt = $("#rentals option:selected").attr("npt");
  };
	
});
