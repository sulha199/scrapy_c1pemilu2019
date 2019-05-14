function onFilterTopTextBoxChanged() {
  topGridOptions.api.setQuickFilter(
    document.getElementById("filter-top-text-box").value
  );
  document.getElementById('jumlah-top-data').innerHTML = topGridOptions.api.getDisplayedRowCount();
}

function loadTopGrid(filename) {
  var gridDiv = document.querySelector("#topGrid");
  new agGrid.Grid(gridDiv, topGridOptions);
  agGrid.simpleHttpRequest({ url: "data/" + filename }).then(function(data) {
    topGridOptions.api.setRowData(data);
    document.getElementById('jumlah-top-data').innerHTML = topGridOptions.api.getDisplayedRowCount();
  });
}
