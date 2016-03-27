app = angular.module('dsmApp', [])

app.controller('frontEndCtrl', function($scope, $http, $interval) {
    //$scope.authorized = true
    $scope.mainstats = {
        uptime: 0
    }
    $scope.tabs = ['chat', 'players']
    $scope.current_tab = 'chat'
    $scope.user = {}
    $scope.timers = {
    }
    $scope.chat = []
    $scope.sendAuthData = function() {
        $http.post('http://'+$scope.user.server+'/auth/', $scope.user, {withCredentials: true}).then(
            function (resp) {
                if (!resp.data.error) {
                    $scope.authorized = true
                }
                else {
                    $scope.error = resp.data.error
                }
            }
        )
        $scope.timers.chat = $interval($scope.checkChat, 1000)
    }
    //timers
    $scope.checkChat = function() {
        console.log($scope.chat)
        if (!$scope.chat.length) {
            console.log(1)
            var req = {}
        }
        else {
            var req = {
                last_id: $scope.chat[$scope.chat.length-1].id
            }
        }
        $http.post('http://'+$scope.user.server+'/chat/get/', req, {withCredentials: true}).then(
            function(resp){
                if (!resp.data.error) {
                    $scope.chat.push.apply($scope.chat, resp.data.chat)
                }
            }
        )
    }
    //tab controls
    $scope.openTab = function(tab) {
        $scope.current_tab = tab
    }
})