(function(){
    "use strict";

    var app = angular.module("pynative");

    app.directive("radiogroupview", function() {
        return {
            controller: "ViewController",
            templateUrl: "/static/angular-templates/radiogroup.html",
            restrict: "E",
            scope: {
                viewdata: "=viewdata"
            }
        };
    });
})();
