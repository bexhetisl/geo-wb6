
class clsbasemaps():
    google_hybrid =  ('Google Hybrid', 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', {
                    'attribution':  'ThanksToGoogleMap',
                    'minZoom': "1",
                    'maxZoom': "21",
                    'subdomains': ['mt0', 'mt1', 'mt2', 'mt3']
    })

    google_satellite=  ('Google Satellite', 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
                    'attribution':  'ThanksToGoogleMap',
                    'minZoom': "1",
                    'maxZoom': "21",
                    'subdomains': ['mt0', 'mt1', 'mt2', 'mt3']
                }) 
 
            
    google_maps= ('Google Maps', 'https://mt1.google.com/vt/lyrs=h&x={x}&y={y}&z={z}', {
                    'attribution':  'ThanksToGoogleMap',
                    'minZoom': "1",
                    'maxZoom': "21",
                    'subdomains': ['mt0', 'mt1', 'mt2', 'mt3']
                })

    openstreetmaps=('OpenStreetMap', 'http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
                'attribution': '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                    'minZoom': "1",
                    'maxZoom': "21",
                })  
    dark_map= ('Drak Map', 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
                    'attribution': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
                    'subdomains': 'abcd',
                    'minZoom': "1",
                    'maxZoom': "21",
                })  
    # bashkite_2014 =  ('bashkite_2014','http://localhost:8080/geoserver/vcad/wms?',
    #                   {
    #                     'layers': 'vcad:bashkite_2014',
    #                     'attribution' : 'vcad:bashkite_2014',
    #                     'overlay': 'True',
    #                     'control':'True',
    #                     'opacity':'1',
    #                     'name':'bashkite_2014',
    #                     'fmt':'image/png',
    #                     'transparent':'True'
    #                     })

    # orthophoto_2015 =('orthophoto_2015',"https://geoportal.asig.gov.al/service/wms",
    #                             {
    #                                 'layers': 'orthophoto_2015:OrthoImagery_20cm',
    #                                 'format': 'image/png',
    #                                 'transparent': 'true',
    #                                 'version': '1.1.0',
    #                                 'attribution': "Albanian Orthophoto 2015"
    #                             }
    #                       )
    # xxx =    ('xxx',"http://localhost:8080/geoserver/vcad/wms?", {
    #     'layers': 'vcad:vineyardunit',
    #     'format': 'image/png',
    #     'transparent': 'true',
    #     'version': '1.1.0',
    #     'attribution': "Weather data © 2012 IEM Nexrad"
    # })

    # foliullayer =   folium.WmsTileLayer(
    #         url="https://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi",
    #         name="test",
    #         fmt="image/png",
    #         layers="nexrad-n0r-900913",
    #         attr=u"Weather data © 2012 IEM Nexrad",
    #         transparent=True,
    #         overlay=True,
    #         control=True,
    #     )
    # leafletlayer = L.tileLayer.wms('http://localhost:8080/geoserver/vcad/wms', {
    #          'layers': 'vcad:vineyardunit',
    #          'transparent': 'true',
    #          "tiled": 'false',
    #          "format": "image/png",
    # })
    
    #dashleaflet=dl.WMSTileLayer(url="http://localhost:8080/geoserver/vcad/wms?",layers="vcad:vineyardunit", format="image/png", transparent=False)
    
    #  var vineyardunit = L.tileLayer.wms('http://localhost:8080/geoserver/vcad/wms', {
    #          layers: 'vcad:vineyardunit',
    #          transparent: true,
    #          "tiled": false,
    #          "format": "image/png",
    # }) 
    
    # ipyleaflet_wms = WMSLayer(
    # url='http://localhost:8080/geoserver/vcad/wms',
    # layers='vcad:vineyardunit',
    # format='image/png',
    # transparent=True,
    # attribution='Weather data © 2012 IEM Nexrad'
    # )