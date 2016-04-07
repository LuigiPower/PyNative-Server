(function(){
    "use strict";

    var app = angular.module("pynative");

    app.directive("textview", function() {
        return {
            controller: "ViewController",
            templateUrl: "/static/angular-templates/textview.html",
            restrict: "E",
            scope: {
                viewdata: "=viewdata"
            }
        };
    });
})();
