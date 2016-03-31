app.factory('AjaxSrv', ['$http', function($http){
    return {
        server: '',
        request: function(url, data, onSuccess, onError) {
            $http.post('http://'+this.server+url, data, {withCredentials: true}).then(onSuccess, onError)
        }
    }
}])