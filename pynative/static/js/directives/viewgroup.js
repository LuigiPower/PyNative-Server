(function(){
    "use strict";

    var app = angular.module("pynative");

    app.directive("viewgroup", function() {
        return {
            controller: "ViewController",
            templateUrl: "/static/angular-templates/viewgroup.html",
            restrict: "E",
            scope: {
                viewdata: "=viewdata"
            }
        };
    });
})();
