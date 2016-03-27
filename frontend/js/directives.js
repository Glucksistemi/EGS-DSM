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

