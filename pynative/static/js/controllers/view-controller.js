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
        $scope.RADIOGROUP = "radiogroup";
        $scope.IMAGE = "imageview";
        $scope.VIEWGROUP = "viewgroup";
        $scope.LINEARLAYOUT = "linearlayout";
        $scope.VIEWSWITCHER = "viewswitcher";


        $scope.isUnknown = function(view)
        {
            return !($scope.isOfType(view, $scope.VIEW)
                    || $scope.isOfType(view, $scope.TEXTVIEW)
                    || $scope.isOfType(view, $scope.BUTTON)
                    || $scope.isOfType(view, $scope.CHECKBOX)
                    || $scope.isOfType(view, $scope.RADIOGROUP)
                    || $scope.isOfType(view, $scope.IMAGE)
                    || $scope.isOfType(view, $scope.VIEWGROUP)
                    || $scope.isOfType(view, $scope.LINEARLAYOUT)
                    || $scope.isOfType(view, $scope.)
                );
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
