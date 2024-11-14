//=====================================================================================================
//shtuar ne 
//D:\ISB\GEO-WB6_AUT_GeoinformationCentre\WinecadGeodjango\winecadroot\geo-wb6-rev09\venv\Lib\site-packages\leaflet\templates\leaflet
//
var selected, features, layer_name, layerControl;
//=====================================================================================================
var orthophoto_2015 = L.tileLayer.wms('https://geoportal.asig.gov.al/service/wms', 
    {
     layers: 'orthophoto_2015:OrthoImagery_20cm',
     transparent: true,
     "tiled": true,
     "format": "image/png",
    }
) ; 
 var vineyardunit = L.tileLayer.wms('http://localhost:8080/geoserver/vcad/wms', {
             layers: 'vcad:vineyardunit',
             transparent: true,
             "tiled": false,
             "format": "image/png",
    }) ;
var referencegrid = L.tileLayer.wms('http://localhost:8080/geoserver/vcad/wms', {
             layers: 'vcad:referencegrid',
             transparent: true,
             "tiled": false,
             "format": "image/png",
    }) ;
  var bashkite_2014 = L.tileLayer.wms('http://localhost:8080/geoserver/vcad/wms', {
        layers: 'vcad:bashkite_2014',
        transparent: true,
        "tiled": false,
        "format": "image/png",
}).addTo(map);
var blockgrid = L.tileLayer.wms('http://localhost:8080/geoserver/vcad/wms', {
             layers: 'vcad:blockgrid',
             transparent: true,
             "tiled": false,
             "format": "image/png",
    }) ;

var google_hybrid =  L.tileLayer(  'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', {
    attribution:  'Google Hybrid',
    minZoom: 1,
    maxZoom: 21,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
});

var google_satellite=  L.tileLayer(  'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    attribution:  'Google satellite',
    minZoom: 1,
    maxZoom: 21,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
}).addTo(map);


var google_maps= L.tileLayer(  'https://mt1.google.com/vt/lyrs=h&x={x}&y={y}&z={z}', {
    attribution:  'Google maps',
    minZoom: 1,
    maxZoom: 21,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
});

 
var dark_map= L.tileLayer( 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
    subdomains: 'abcd',
    minZoom: 1,
    maxZoom: 21,
    attribution: '© Dark Map'
});
//=====================================================================================================
const osm = "https://www.openstreetmap.org/copyright";
const copy = `© <a href='${osm}'>OpenStreetMap</a>`;
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osmlayer = L.tileLayer(url, { attribution: copy });
//============================================================================================
var mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +    'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>';
var mbUrl = 'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiYmV4aGV0aXNsIiwiYSI6ImNrZng1ajE4MzA2aGwycm5reGkzcWZjZTUifQ.1EiXwgJKX2iEY4vzDmTj8w';
var streetslayer  = L.tileLayer(mbUrl, {id: 'mapbox/streets-v11', tileSize: 512, zoomOffset: -1, attribution: mbAttr});
//============================================================================================
var openstreetmap=L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '© OpenStreetMap contributors'
});

var baseLayers = {
    "Google hybrid": google_hybrid,
    "Google satellite": google_satellite,
    "google_maps": google_maps,
    "OpenStreetMap": openstreetmap,
    "Streets layer": streetslayer,
    "Dark map": dark_map,
};
var overlays = {
    "orthophoto 2015": orthophoto_2015,
    "bashkite_2014":bashkite_2014,
    "referencegrid": referencegrid,
    "blockgrid": blockgrid,
    "vineyardunit": vineyardunit,
 
};
L.control.layers(baseLayers, overlays)  

L.control.scale({position:'bottomright', imperial: false}).addTo(map);

L.control.polylineMeasure({
    position: 'topleft',
    unit: 'kilometres',
    showBearings: true,
    clearMeasurementsOnStop: false,
    showClearControl: true,
    showUnitControl: true
}).addTo(map);
  
var measureControl = new L.Control.Measure({
    position: 'topleft'
});
measureControl.addTo(map);

  