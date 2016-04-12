(function(){
    "use strict";

    var app = angular.module("pynative");

    app.directive("checkboxview", function() {
        return {
            controller: "ViewController",
            templateUrl: "/static/angular-templates/checkbox.html",
            restrict: "E",
            scope: {
                viewdata: "=viewdata"
            }
        };
    });
})();
