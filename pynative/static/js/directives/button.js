(function(){
    "use strict";

    var app = angular.module("pynative");

    app.directive("buttonview", function() {
        return {
            controller: "ViewController",
            templateUrl: "/static/angular-templates/button.html",
            restrict: "E",
            scope: {
                viewdata: "=viewdata"
            }
        };
    });
})();
