(function(){
    "use strict";

    var app = angular.module('pynative');

    app.directive("viewswitcher", function() {
        return {
            controller: "SwitchController",
            templateUrl: "/static/angular-templates/viewswitcher.html",
            restrict: "E",
            scope: {
                view: "=view"
            }
        };
    });
})();
