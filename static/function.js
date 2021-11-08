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


