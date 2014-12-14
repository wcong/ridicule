angular.module('redicule', []).
  config(['$routeProvider', function($routeProvider) {
  $routeProvider.
      when('/login', {templateUrl: 'partials/phone-list.html',   controller: PhoneListCtrl}).
      when('/home', {templateUrl: 'partials/phone-detail.html', controller: PhoneDetailCtrl}).
      when('/setting', {templateUrl: 'partials/phone-detail.html', controller: PhoneDetailCtrl}).
      when('/invite', {templateUrl: 'partials/phone-detail.html', controller: PhoneDetailCtrl}).
      otherwise({redirectTo: '/home'});
}]);
function index($scope){
}
function login($scope){
}
function setting($scope){
}
function invite($scope){
}