myApp.factory('myFactory', function($http){

	var batch_id;
	return {
		getStatus: function(callback){
			//console.log($scope.ccapName);
			$http({
				method: 'GET',
				url: '/status',
				cache: false
			}).success(callback);
		},
		startBatch: function ($scope,callback){ 
		 $http({
				method: 'POST',
				url: '/startBatch',
				data: $scope.user,
				cache: false
			}).success(callback);
		},
		populatePage: function($scope){
					$http({
					  method: 'GET',
					  url: '/getFiles',
					  cache: false
					}).then(function successCallback(response) {
						$scope.templates = response.data.template;
						$scope.asset_files = response.data.asset;
						$scope.mac_files = response.data.mac;
						$scope.avns = response.data.avn;
						$scope.headends = response.data.headend;
					  }, function errorCallback(response) {
						console.log('fail');
					  });
		},
		loadTemplate: function($scope,callback){
			//console.log($scope.ccapName);
			$http({
				method: 'GET',
				url: '/loadTemplate',
				params: {config:$scope.user.template},
				cache: false
			}).success(callback);
		},
		saveTemplate: function($scope,callback,errorCallBack){
			//console.log($scope.ccapName);
			$http({
				method: 'POST',
				url: '/saveTemplate',
				data:  $scope.user,
				cache: false
			}).success(callback).error(errorCallBack);
		},
		showBatch: function ($scope,callback,errorCallBack){ 
		 $http({
				method: 'GET',
				url: '/showBatch/'+$scope.batchID,
				cache: false
			}).success(callback).error(errorCallBack);
		},
		stopBatch: function ($scope,callback,errorCallBack){ 
		 $http({
				method: 'POST',
				url: '/stopBatch/'+$scope.batchID,
				cache: false
			}).success(callback).error(errorCallBack);
		},
		fetchReport: function($scope,callback,errorCallBack){
					$http({
					  method: 'GET',
					  url: '/fetchReport',
					  cache:false
					}).success(callback).error(errorCallBack);
		},
		setbatch: function(batch){			
			batch_id = batch;			
		},
		getbatch: function(){
			return batch_id;
		}
	};
});