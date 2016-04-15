app.factory('AjaxSrv', ['$http', function($http){
    return {
        server: '',
        request: function(url, data, onSuccess, onError) {
            $http.post('http://'+this.server+url, data, {withCredentials: true}).then(onSuccess, onError)
        },
        get: function(url, data, target, error) {
            $http.post(
                'http://'+this.server+url,
                data,
                {withCredentials: true}
            ).then(
                function(resp){
                    if (!resp.data.error) {
                        target = resp.data
                        error = false
                    }
                    else {
                        error = resp.data.error
                    }
                },
                function(resp){
                    error = resp.status
                }
            )
        }
    }
}])
//
//app.factory('TerminalSrv', ['AjaxSrv', '$interval', '$timeout', function(AjaxSrv, $interval, $timeout){ return {
//    lines: [],
//    concatLines: function(resp) {
//        this.lines = this.lines.concat(resp.data)
//    },
//    loadBuffer: function(){
//        AjaxSrv.request(
//            '/terminal/get/',
//            {},
//            this.concatLines
//        )
//    },
//    sendCommand: function(command, onSuccess, onError) {
//        AjaxSrv.request(
//            '/terminal/send/',
//            {command: command},
//            function(resp) {
//                onSuccess(resp)
//                $timeout(this.loadBuffer, 100)
//            },
//            onError
//        )
//    }
//}}])