var ShopAppInstance = new ShopApp(function(app) {
    app.init(null, function(params, app) {
        if (localStorage.getItem('styles') === null) {
            for(var x = 0; x < params.styles.length; ++x) {
                var el = document.createElement('link');
                el.rel = 'stylesheet';
                el.type = 'text/css';
                el.href = params.styles[x];
                document.getElementsByTagName('head')[0].appendChild(el);     
            }
        }
        localStorage.setItem('styles', JSON.stringify(params.styles));

        app.show(null ,function () {
            app.adjustIframeSize();
        });
    }, function(errmsg, app) {
        alert(errmsg);
    });
}, true);