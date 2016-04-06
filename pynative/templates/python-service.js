(function(){
    "use strict";

    var app = angular.module("python-module", []);

    app.service("python-service", [ function() {
        var context = this;

        console.log("Cose");
        {% if data is defined %}
        this.data = {{ data | safe }};
        {% else %}
        this.data = {};
        {% endif %}

        console.log("Data is");
        console.log(this.data);

    }]);

})();
