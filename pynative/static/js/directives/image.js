(function(){
    "use strict";

    var app = angular.module("pynative");

    app.directive("imageview", function() {
        return {
            controller: "ViewController",
            templateUrl: "/static/angular-templates/imageview.html",
            restrict: "E",
            scope: {
                viewdata: "=viewdata"
            }
        };
    });
})();
