(function(){
    "use strict";

    var app = angular.module('pynative');

    app.controller("ViewController", ['$scope', 'session-service', function($scope, session) {

        console.log($scope.viewdata);

        if(!$scope.viewdata)
        {
            $scope.viewdata = {};
        }

        $scope.getParameter = function(parameter)
        {
            return $scope.viewdata['parameters'][parameter];
        };

        $scope.getType = function()
        {
            return $scope.viewdata['type'];
        };

        $scope.getLayout = function()
        {
            return $scope.viewdata['parameters']['layout'];
        };

        $scope.getViews = function()
        {
            return $scope.viewdata['parameters']['layout']['views'];
        };

        $scope.getEvents = function()
        {
            return $scope.viewdata['parameters']['events'];
        };
    }]);

})();
