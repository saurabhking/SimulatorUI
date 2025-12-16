var myApp = angular.module('myApp', ['ngRoute']);
var refreshTimer;
myApp.config(function($routeProvider) {
	$routeProvider.
	when('/', {
		templateUrl: '/main',
		controller: 'MainCtrl'
	}).
	when('/stats', {
		templateUrl: 'stats',
		controller: 'StatsCtrl'
	}).
	when('/report', {
		templateUrl: 'report',
		controller: 'ReportCtrl'
	}).
	otherwise({
		redirectTo: '/'
	});
	
});