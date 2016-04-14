(function(){
    "use strict";

    var app = angular.module("pynative");

    app.directive("viewswitcher", function() {
        return {
            controller: "ViewController",
            templateUrl: "/static/angular-templates/viewswitcher.html",
            restrict: "E",
            scope: {
                viewdata: "=viewdata"
            }
        };
    });
})();
