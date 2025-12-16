myApp.factory('myFactory', function($http){

	var batch_id;
	return {
		start: function ($scope,callback){ 
		 $http({
				method: 'POST',
				url: '/session/start',
				data: $scope.user,
				cache: false
			}).success(callback);
		},
		play: function ($scope,callback){ 
		 $http({
				method: 'POST',
				url: '/session/play',
				data: $scope.user,
				cache: false
			}).success(callback);
		},
		pause: function ($scope,callback){ 
		 $http({
				method: 'POST',
				url: '/session/pause',
				data: $scope.user,
				cache: false
			}).success(callback);
		},
		ff: function ($scope,callback){ 
		 $http({
				method: 'POST',
				url: '/session/ff',
				data: $scope.user,
				cache: false
			}).success(callback);
		},
		rw: function ($scope,callback){ 
		 $http({
				method: 'POST',
				url: '/session/rw',
				data: $scope.user,
				cache: false
			}).success(callback);
		},
		teardown: function ($scope,callback){ 
		 $http({
				method: 'POST',
				url: '/session/teardown',
				data: $scope.user,
				cache: false
			}).success(callback);
		},
		asset: function ($scope,callback){ 
		 $http({
				method: 'GET',
				url: '/session/asset',
				cache: false
			}).success(callback);
		},
		getaccount: function ($scope,callback){ 
		 $http({
				method: 'POST',
				url: '/session/getaccount',
				data: $scope.user,
				cache: false
			}).success(callback);
		}
	};
});