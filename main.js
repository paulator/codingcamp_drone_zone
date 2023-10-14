// var jsonData = "./assets/json/koordinaten_test.json"
var table = document.getElementById("table");
var tableBody = document.getElementById("table-body");
var loader = document.getElementById("loader")

// Loop through the data and generate table rows
for (var i = 0; i < jsonData.length; i++) {
    if (jsonData[i].muell_gefunden === true) {

        var row = tableBody.insertRow();
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        var cell5 = row.insertCell(4);

        cell1.textContent = i;
        var image = document.createElement("img");
        image.src = './output/' + jsonData[i].filename;
        image.width = 300; // Set image width
        image.height = 200; // Set image height
        cell2.appendChild(image);
        cell3.textContent = jsonData[i].latitude;
        cell4.textContent = jsonData[i].longitude;
        var checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        cell5.appendChild(checkbox);
    }
}
setTimeout(() => {
    table.style = "opacity:1;";
    loader.style = "display:none !important;";
}, 2000);
