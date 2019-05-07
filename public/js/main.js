var columnDefs = [
  {
    headerName: "Propinsi",
    field: "propinsi",
    width: 150
  },
  {
    headerName: "Kab/Kota",
    field: "kab",
    width: 150
  },
  {
    headerName: "Kecamatan",
    field: "kec",
    width: 150
  },
  {
    headerName: "Kelurahan",
    field: "kel",
    width: 150
  },
  {
    headerName: "TPS",
    field: "tps",
    width: 70
  },
  {
    headerName: "pemilu2019.kpu.go.id/",
    children: [
      { headerName: "01", field: "p1", width: 70 },
      { headerName: "02", field: "p2", width: 70 }
    ]
  },
  {
    headerName: "pantau.kawalpilpres2019.id",
    children: [
      { headerName: "01", field: "kawal_p1", width: 70 },
      { headerName: "02", field: "kawal_p2", width: 70 }
    ]
  }
];

var gridOptions = {
  defaultColDef: {
    sortable: true,
    resizable: true,
    filter: true
  },
  debug: true,
  columnDefs: columnDefs,
  rowData: []
};

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
  agGrid.simpleHttpRequest({ url: "data/" + filename }).then(function(data) {
    gridOptions.api.setRowData(data);
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
