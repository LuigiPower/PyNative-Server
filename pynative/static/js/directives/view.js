(function(){
    "use strict";

    var app = angular.module("pynative");

    app.directive("view", function() {
        return {
            controller: "ViewController",
            templateUrl: "/static/angular-templates/view.html",
            restrict: "E",
            scope: {
                viewdata: "=viewdata"
            }
        };
    });
})();
