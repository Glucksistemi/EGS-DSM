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

