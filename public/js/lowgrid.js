function onFilterLowTextBoxChanged() {
  lowGridOptions.api.setQuickFilter(
    document.getElementById("filter-low-text-box").value
  );
  document.getElementById('jumlah-low-data').innerHTML = lowGridOptions.api.getDisplayedRowCount();
}

function loadLowGrid(filename) {
  var gridDiv = document.querySelector("#lowGrid");
  new agGrid.Grid(gridDiv, lowGridOptions);
  agGrid.simpleHttpRequest({ url: "data/" + filename }).then(function(data) {
    lowGridOptions.api.setRowData(data);
    document.getElementById('jumlah-low-data').innerHTML = lowGridOptions.api.getDisplayedRowCount();
  });
}
