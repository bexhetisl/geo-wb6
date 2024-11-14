
import os
#template_widget_path_isb="D:\ISB\GEO-WB6_AUT_GeoinformationCentre\WinecadGeodjango\winecadroot\geo-wb6-rev10\venv\Lib\site-packages\leaflet\templates\leaflet"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
ROOT_URLCONF = 'winecad.urls'


SECRET_KEY = 'django-insecure-a4bvevc00#2zbe=w7qyd(t_xx&e6q4&5em&*%994h(=z2l1(-)'

DEBUG = True

ALLOWED_HOSTS = ['*']

os.environ['PROJ_LIB'] = r'C:\Users\Flooding_ISB\.conda\pkgs\proj-9.5.0-hd9569ee_0\Library\share\proj'
#os.environ['GDAL_DATA'] = r'C:\Program Files\GDAL\bin\gdal-data'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'leaflet',
    'djgeojson',
    'mapwidgets',
    'admin_reorder',
    'location_field.apps.DefaultConfig',
    'winecadapp',
         
]

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [os.path.join(BASE_DIR, "templates"), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
              
            ],
        },
    },
]

WSGI_APPLICATION = 'winecad.wsgi.application'

DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME':   'winecadnewuser',#'winecadnewuser', #
            'USER':   'postgres',
            'PASSWORD':   'P1g0l1n0',
            'HOST': '127.0.0.1',
            'PORT':   5432,
        }}

GEOS_LIBRARY_PATH = r'C:\OSGeo4W\bin\geos_c'
GDAL_LIBRARY_PATH  = r'C:\OSGeo4W\bin\gdal309'
#GDAL_LIBRARY_PATH  =r"D:\ISB\GEO-WB6_AUT_GeoinformationCentre\WinecadGeodjango\winecadroot\geo-wb6-rev07\venv\Lib\site-packages\GDAL-3.6.2-py3.9-win-amd64.egg-info"

SERIALIZATION_MODULE={
    'geojson':'djgeojson.serializers'
}
 
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en', 'English'),
    ('al', 'Albanian'),
]
    

MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
ADMINS = ['erik.islamaj@gmail.com']

MAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

 
EMAIL_USE_TLS = True
EMAIL_HOST ='smtp.googlemail.com'
EMAIL_HOST_USER = 'erik.islamaj@gmail.com'
EMAIL_HOST_PASSWORD = 'ubnp cawk hkbe iwzg'
EMAIL_PORT= 587

MAIL_USE_TLS = 0
MAIL_USE_SSL = 1

POSTS_PER_PAGE = 25


TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

LEAFLET_CONFIG = {
    # conf here
# 'PLUGINS': {
#     'forms': {'auto-include': True},
#     'fullscreen': {
#         'css': ['/static/css/leaflet.fullscreen.css', ],
#         'js': ['/static/js/Leaflet.fullscreen.min.js', ],
#         'auto-include': True
#     },
# },
    
'DEFAULT_CENTER': (40, 20),
'CENTER':(40, 20),
'DEFAULT_ZOOM': 16,
'MIN_ZOOM': 1,
'MAX_ZOOM':20 ,
'DEFAULT_PRECISION': 6,
'WIDTH':'600px',
'HEIGHT':'600px',
'overlayPane' : {
  "Endpoints" : 'endpointMarkerLayer',
  "Links" : 'linkLineLayer',
},
    #============
 #'map_template' :'gis/admin/openlayers_extralayers.html',
 
'RESET_VIEW': False,
        'TILES':     [
                        # clsbasemaps.google_hybrid,
                        # clsbasemaps.google_satellite,
                        # clsbasemaps.google_maps,
                        # #clsbasemaps.openstreetmaps,
                        # clsbasemaps.dark_map,
 
                    ],
        'OVERLAYS': [
                        #clsbasemaps.ipyleaflet_wms
                    ]
    ,}

#'TILES': 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
#https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MAP_WIDGETS = {
    "GoogleMap": {
        "apiKey": 'AIzaSyA5g6bFK2t-0zQbCGT-uy_owEDm07_2oBc', #GOOGLE_MAP_API_KEY # General setting for all GoogleMap widgets
        "PointField": {   # GeoField type
            "interactive": {  # Specific settings for GoogleMap interactive PointField widget
                "mapOptions": {
                    "zoom": 15,
                },
                "GooglePlaceAutocompleteOptions": {
                    "componentRestrictions": {"country": "al"}
                },
                "mapCenterLocationName": "Tirana",
            }
        },
    },
    "Mapbox": {
        "accessToken": 'pk.eyJ1IjoiYmV4aGV0aXNsIiwiYSI6ImNrZng1ajE4MzA2aGwycm5reGkzcWZjZTUifQ.1EiXwgJKX2iEY4vzDmTj8w',#MAPBOX_ACCESS_TOKEN,
        "PointField": {
            "interactive": {
                "mapOptions": {"zoom": 12, "center": (40, 20)},
                "markerFitZoom": 14,
            }
        },
    },
    "is_dev_mode": False,  # Package global level setting for development mode
}


ADMIN_REORDER = (
   {
        'app': 'auth',  # The app name
        'label': 'Authentication and Authorization',  # The label you want to display
        'models': ('auth.User', 'auth.Group'),  # List the models in the order you want
    },
    {
        'app': 'winecadapp',  # Replace this with your app's actual name
        'label': 'Winecad Layers', 
        'models': ('winecadapp.vineyardunit', 'winecadapp.bashkite_2014', 'winecadapp.blockgrid',   'winecadapp.villages', 
                   'winecadapp.qarqet', 'winecadapp.referencegrid', 'winecadapp.blockgrid', 'winecadapp.totalrowsvineyardalbania'),  # Replace with your actual models
    },
    {
        'app': 'winecadapp',  # Replace this with your app's actual name
        'label': 'Winecad tables', 
        'models': ('winecadapp.person' ,),  # Replace with your actual models
    },
   {
        'app': 'winecadapp',  # Replace this with your app's actual name
        'label': 'Winecad tables', 
        'models': ('winecadapp.soiltype', 'winecadapp.exposure', 'winecadapp.productiontype', 'winecadapp.soiltype', 
                  'winecadapp.inclination', 'winecadapp.mechanizationtype', 'winecadapp.rowsdirection', 'winecadapp.soildepth', 
                  'winecadapp.cultivationform', 'winecadapp.cultivationtype', 'winecadapp.supporttype', 'winecadapp.rocktype', 
                  'winecadapp.varietypurity', 'winecadapp.irrigationtype', 'winecadapp.rowsdirectiontype', 'winecadapp.surveystate', 
                   'winecadapp.exposure','winecadapp.rootstock'),  # Replace with your actual models
    },
)
               
#ROOT_URLCONF = 'tests.test_urls'
MEDIA_ROOT = os.path.join(BASE_DIR, "tmp")
MEDIA_URL = '/media/'

