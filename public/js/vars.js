var __basePath = "";
var headerHeight = 90;
var columnDefs = [
  {
    headerName: "Propinsi",
    field: "propinsi",
    width: 140,
    sortable: true
  },
  {
    headerName: "Kab/Kota",
    field: "kab",
    width: 140,
    sortable: true
  },
  {
    headerName: "Kecamatan",
    field: "kec",
    width: 140,
    sortable: true
  },
  {
    headerName: "Kelurahan",
    field: "kel",
    width: 140,
    sortable: true
  },
  {
    headerName: "TPS",
    field: "tps",
    width: 70,
    sortable: true
  },
  {
    headerName: "pemilu2019.kpu.go.id/",
    children: [
      {
        headerName: "01",
        field: "p1",
        width: 70,
        sortable: true,
        cellStyle: { "background-color": "#bde2e5" }
      },
      {
        headerName: "02",
        field: "p2",
        width: 70,
        sortable: true,
        cellStyle: { "background-color": "#cec" }
      },
      {
        headerName: "Suara Valid",
        field: "suara_valid",
        width: 70,
        sortable: true,
        cellStyle: { "background-color": "#ececec" }
      },
      {
        headerName: "DPT awal",
        field: "dpt",
        width: 70,
        sortable: true,
        cellStyle: { "background-color": "#ececec" }
      },
      {
        headerName: "Presentase Suara Valid / DPT (%)",
        field: "presentase",
        width: 110,
        sortable: true,
        cellStyle: { "background-color": "#ececec" }
      }
    ]
  },
  {
    headerName: "pantau.kawalpilpres2019.id",
    children: [
      {
        headerName: "01",
        field: "kawal_p1",
        width: 70,
        sortable: true,
        cellStyle: { "background-color": "#bde2e5" }
      },
      {
        headerName: "02",
        field: "kawal_p2",
        width: 70,
        sortable: true,
        cellStyle: { "background-color": "#cec" }
      }
    ]
  },
  {
    headerName: "ayojagatps.com",
    children: [
      {
        headerName: "01",
        field: "ayo_p1",
        width: 70,
        sortable: true,
        cellStyle: { "background-color": "#bde2e5" }
      },
      {
        headerName: "02",
        field: "ayo_p2",
        width: 70,
        sortable: true,
        cellStyle: { "background-color": "#cec" }
      }
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
  rowData: [],
  groupHeaderHeight: 45,
  headerHeight: headerHeight
};

var topGridOptions = {
  defaultColDef: {
    sortable: true,
    resizable: true,
    filter: true
  },
  debug: true,
  columnDefs: columnDefs,
  rowData: [],
  groupHeaderHeight: 45,
  headerHeight: headerHeight
};

var lowGridOptions = {
  defaultColDef: {
    sortable: true,
    resizable: true,
    filter: true
  },
  debug: true,
  columnDefs: columnDefs,
  rowData: [],
  groupHeaderHeight: 45,
  headerHeight: headerHeight
};

var notGridOptions = {
  defaultColDef: {
    sortable: true,
    resizable: true,
    filter: true
  },
  debug: true,
  columnDefs: columnDefs,
  rowData: [],
  groupHeaderHeight: 45,
  headerHeight: headerHeight
};
