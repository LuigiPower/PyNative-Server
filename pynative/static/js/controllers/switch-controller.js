(function(){
    "use strict";

    var app = angular.module('pynative');

    app.controller("SwitchController", ['$scope', 'session-service', function($scope, session) {

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
                );
        };

        $scope.isOfType = function(viewtype, viewcompare)
        {
            return viewtype === viewcompare;
        };
    }]);

})();
