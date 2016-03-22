app = angular.module('dsmApp', [])

app.controller('frontEndCtrl', function($scope, $http, $interval) {
    //$scope.authorized = true
    $scope.mainstats = {
        uptime: 0
    }
    $scope.timers = {
    }
    $scope.sendAuthData = function() {
        $scope.authorized = true
        $scope.timers.chat = $interval($scope.checkChat, 1000)
    }
    $scope.checkChat = function() {
        $scope.mainstats.uptime += 1
    }
})