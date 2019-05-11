function onFilterNotTextBoxChanged() {
    notGridOptions.api.setQuickFilter(
      document.getElementById("filter-not-text-box").value
    );
  }
  
  function loadNotGrid(filename) {
    var gridDiv = document.querySelector("#notGrid");
    new agGrid.Grid(gridDiv, notGridOptions);
    agGrid.simpleHttpRequest({ url: "data/" + filename }).then(function(data) {
      notGridOptions.api.setRowData(data);
    });
  }
  