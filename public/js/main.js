file_list = [];

function getFileList() {
  $.get(
    "https://raw.githubusercontent.com/sulha199/scrapy_c1pemilu2019/master/public/data/file_list.txt",
    data => {
      file_list = data.split("\n");
      latestKomparasi = getKomparasiList(file_list);
      fileParam = getUrlVars();
      loadOldVersionList(latestKomparasi);
      loadKomparasiData(fileParam["file"] || latestKomparasi[0]);
    }
  );
}

function loadKomparasiData(filename) {
  selectedData = filename.replace("komparasi_", "");
  agGrid.simpleHttpRequest({ url: "data/" + filename }).then(function(data) {
    gridOptions.api.setRowData(data);
    loadTopGrid("toplist_" + selectedData);
    loadLowGrid("lowlist_" + selectedData);
    loadNotGrid("notlist_" + selectedData);
    $("#data-time").html(
      filename
        .replace("komparasi_", "")
        .replace(".json", "")
        .replace("_", " ")
        .replace(".", ":")
    );
  });
}

function getKomparasiList(list) {
  return list
    .filter(d => d.includes("komparasi_"))
    .sort()
    .reverse();
}

function getKpuDataList(list) {
  return list
    .filter(d => d.includes("kpu_"))
    .sort()
    .reverse();
}

function getKawalDataList(list) {
  return list
    .filter(d => d.includes("kawal_"))
    .sort()
    .reverse();
}

function loadOldVersionList(list) {
  list.map(filename => {
    $("#komparasi-list").append(
      '<li><a href="?file=' + filename + '">' + filename + "</a></li>"
    );
  });
}

function openVersions() {
  $("#old-version-selector").dialog();
}

function onFilterTextBoxChanged() {
  gridOptions.api.setQuickFilter(document.getElementById('filter-text-box').value);
}

document.addEventListener("DOMContentLoaded", function() {
  var gridDiv = document.querySelector("#myGrid");
  new agGrid.Grid(gridDiv, gridOptions);

  getFileList();
});
