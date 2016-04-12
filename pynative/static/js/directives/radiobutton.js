(function(){
    "use strict";

    var app = angular.module("pynative");

    app.directive("radiobuttonview", function() {
        return {
            controller: "ViewController",
            templateUrl: "/static/angular-templates/radiobutton.html",
            restrict: "E",
            scope: {
                viewdata: "=viewdata"
            }
        };
    });
})();
