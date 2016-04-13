(function(){
    "use strict";

    var app = angular.module('pynative');

    app.controller("ViewController", ['$scope', 'session-service', function($scope, session) {

        console.log($scope.viewdata);

        $scope.UNKNOWN = "__";
        $scope.VIEW = "view";
        $scope.TEXTVIEW = "textview";
        $scope.BUTTON = "button";
        $scope.CHECKBOX = "checkbox";
        $scope.RADIOBUTTON = "radiobutton"
        $scope.IMAGE = "imageview"


        $scope.isUnknown = function(view)
        {
            return !($scope.isOfType(view, $scope.VIEW)
                    || $scope.isOfType(view, $scope.TEXTVIEW)
                    || $scope.isOfType(view, $scope.BUTTON)
                    || $scope.isOfType(view, $scope.CHECKBOX)
                    || $scope.isOfType(view, $scope.RADIOBUTTON)
                    || $scope.isOfType(view, $scope.IMAGE))
        };

        $scope.isOfType = function(viewtype, viewcompare)
        {
            return viewtype === viewcompare;
        };


        //$scope.viewtype is initialized from directive
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
