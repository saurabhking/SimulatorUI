var myApp = angular.module('myApp', ['ngRoute']);
var refreshTimer;
myApp.config(function($routeProvider) {
	$routeProvider.
	when('/', {
		templateUrl: 'main',
		controller: 'MainCtrl'
	}).
	otherwise({
		redirectTo: '/'
	});
	
});