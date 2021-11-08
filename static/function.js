function get_list(kategoria) {
  console.log(kategoria);
  $.ajax({
    type: "GET",
    url: "/api/v1/" + kategoria,
    success: function (potrawy) {
      console.log(potrawy);
      document.querySelector("table.table.table-image tbody").innerHTML = " ";
      for (var potrawa of potrawy) {
        var tdIMG = document.createElement("TD");
        tdIMG.innerHTML = "";
        var img = document.createElement("img");
        img.src = potrawa.image.html;
        img.alt = "Potrawa";
        img.width = "300";
        img.height = "200";
        tdIMG.appendChild(img);
        var tdNAZWA = document.createElement("TD");
        tdNAZWA.innerHTML = potrawa.nazwa;

        var tdPRZEPIS = document.createElement("TD");
        tdPRZEPIS.innerHTML = potrawa.przepis;
        var tr = document.createElement("TR");
        tr.appendChild(tdIMG);
        tr.appendChild(tdNAZWA);
        tr.appendChild(tdPRZEPIS);

        document.querySelector("table.table.table-image tbody").appendChild(tr);
      }
    },
  });
}


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