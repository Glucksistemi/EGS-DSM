app = angular.module('dsmApp', ['ngCookies'])

app.controller('frontEndCtrl', function($scope, $http, $interval, $cookies, AjaxSrv) {
    //$scope.authorized = true
    $scope.mainstats = {
        uptime: 0
    }
    $scope.tabs = ['chat', 'players', 'system', 'config']
    $scope.current_tab = 'chat'
    $scope.user = {
        server: $cookies.get('last-server'),
        login: 'gluck',//TODO: remove it from here after testing done
        password: '123'
    }
    $scope.timers = {
    }
    $scope.chat = []
    $scope.sendAuthData = function() {
        $http.post('http://'+$scope.user.server+'/auth/', $scope.user, {withCredentials: true}).then(
            function (resp) {
                if (!resp.data.error) {
                    $scope.authorized = true
                    $cookies.put('last-server', $scope.user.server)
                    AjaxSrv.server = $scope.user.server
                }
                else {
                    $scope.error = resp.data.error
                }
            }
        )
        $scope.timers.chat = $interval($scope.checkChat, 10000)
        $scope.checkHeartBeat()
        $scope.timers.heartbeat = $interval($scope.checkHeartBeat, 60000)
    }
    //timers
    $scope.checkChat = function() {
        if (!$scope.chat.length) {
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
    $scope.checkHeartBeat = function() {
        $http.post('http://'+$scope.user.server+'/heartbeat/', {}, {withCredentials: true}).then(
            function(resp) {
                $scope.mainstats = resp.data
            }
        )
    }
    //tab controls
    $scope.openTab = function(tab) {
        $scope.current_tab = tab
    }
})