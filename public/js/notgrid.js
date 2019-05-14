function onFilterNotTextBoxChanged() {
    notGridOptions.api.setQuickFilter(
      document.getElementById("filter-not-text-box").value
    );
    document.getElementById('jumlah-not-data').innerHTML = notGridOptions.api.getDisplayedRowCount();
  }
  
  function loadNotGrid(filename) {
    var gridDiv = document.querySelector("#notGrid");
    new agGrid.Grid(gridDiv, notGridOptions);
    agGrid.simpleHttpRequest({ url: "data/" + filename }).then(function(data) {
      notGridOptions.api.setRowData(data);
      document.getElementById('jumlah-not-data').innerHTML = notGridOptions.api.getDisplayedRowCount();
    });
  }
  