app.directive('chat', ['$http', function($http) {
    return {
        scope: {
            messages: '=',
            server: '='
        },
        restrict: 'AE',
        templateUrl: 'templates/chat.html',
        link: function($scope) {
            $scope.sending = false
            $scope.sendMessage = function(){
                if (!$scope.new_message) {
                    return
                }
                $scope.sending = true
                $http.post(
                    'http://'+$scope.server+'/chat/send/',
                    {'message': $scope.new_message},
                    {withCredentials: true}).then(function (response) {
                    $scope.new_message = ''
                    $scope.sending = false
                },
                function(response) {
                    $scope.sending = false
                    $scope.error = response.status
                })
            }
        }
    }
}])
app.directive('system', ['$http', function($http){
    return {
        scope: {
            server: '='
        },
        restrict: 'AE',
        templateUrl: 'templates/system.html',
        link: function($scope) {
            $scope.rebooting = false
            $scope.restartServer = function() {
                $scope.rebooting = true
                $http.post(
                    'http://'+$scope.server+'/restart/', {},
                    {withCredentials: true}).then(function (response) {
                        $scope.rebooting = false
                    }
                )
            }
            $scope.updateCoreLog = function() {
                console.log(111)
                $http.post(
                    'http://'+$scope.server+'/corelog/', {},
                    {withCredentials: true}).then(function(resp) {
                        $scope.corelogdata = resp.data
                    }
                )
            }
            $scope.updateCoreLog()
        }
    }
}])
app.directive('pfconfig', ['$http', function($http) {
    return {
        scope: {
            server: '=',
        },
        restrict: 'AE',
        templateUrl: 'templates/configs.html',
        link: function($scope) {
            $scope.updateConfig = function(){
                $http.post('http://'+$scope.server+'/config/playfield/load', {}, {withCredentials: true}).then(function(resp){
                    $scope.playfields = resp.data
                })
            }
            $scope.saveConfig = function(){
                $http.post('http://'+$scope.server+'/config/playfield/save', $scope.playfields, {withCredentials: true}).then(function(resp){
                    $scope.state = "Succesfully saved!"
                })
            }
        }
    }
}])
app.directive('players', ['$http', function($http){
    return {
        scope: {
            server: '='
        },
        restrict: 'AE',
        templateUrl: 'templates/players.html',
        link: function($scope) {
            $scope.actions = {
                ban: function(steam_id) {
                    var reason = prompt('Reason to ban:', "because fuck you, that's why!")
                    var term = prompt('Time to be banned', '1h')
                    return {
                        steam_id: steam_id,
                        action: 'ban',
                        reason: reason,
                        term: term
                    }
                },
                kick: function(steam_id) {
                    return {
                        steam_id: steam_id,
                        action: 'kick',
                        reason: prompt('Reason to kick:', "I just don't like you")
                    }
                },
                ban_9000: function(steam_id){
                    var reason = prompt('Reason to ban:', "You are a real asshole!")
                    return {
                        steam_id: steam_id,
                        action: 'ban',
                        reason: reason,
                        term: '9000d'
                    }
                },
                unban: function(steam_id) {
                    return {
                        steam_id: steam_id,
                        action: 'unban'
                    }
                }
            }
            $scope.players = []
            $scope.updateList = function (){
                //TODO: http request
            }
            $scope.sendAction(player) {
                
            }
        }
    }
}])
