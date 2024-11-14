#from django.contrib.gis.admin import GISModelAdmin
from django.contrib import admin  as AdminSite
from django.contrib.gis.db import models as gis_models
from mapwidgets.widgets import GoogleMapPointFieldWidget
 
from leaflet.admin import LeafletGeoAdmin


#from import_export import resources


from .models import totalrowsvineyardalbania,vineyardunit, villages ,variety,person,surveystate, productiontype  \
                    ,inclination,mechanizationtype,rowsdirection,soildepth \
                    , blockgrid,cultivationform,cultivationtype \
                    ,supporttype,varietypurity \
                     , bashkite_2014  \
                    ,qarqet,exposure,rocktype,soiltype,rootstock \
                    ,rowsdirectiontype, irrigationtype \
                    ,referencegrid, user
                    
                    
AdminSite.site.site_header = "GEO-WB6 Portal"
AdminSite.site.site_title = "GEO-WB6 Portal"
AdminSite.site.index_title = "GEO-WB6 Portal"

AdminSite.site.site_url="/winecadapp"

AdminSite.site.index_template="./admin/index.html"

change_form_template = "admin/change_form_isb.html"
#admin.site.index_template = 'index_isb.html'
AdminSite.enable_nav_sidebar=True
# app_name = "leaflet"
 
                
class DomainAdmin(AdminSite.ModelAdmin):
    list_display = [ 'code','description'] 
    list_filter =list_display
    search_fields=list_display 
    class Meta:
         ordering = ["code","description"  ]
         

class totalrowsvineyardalbaniaAdmin(LeafletGeoAdmin):
    
    
    list_display=("id", "drejtimi_i_rreshtave", "ekspozimi", "tipi_i_kultivimit", "thellesi_e_tokes", "tipi_i_tokes_meparshme", "shkembi_amnor", 
                "tipi_i_tokes", "lartesia_mumimale_e_kultivimit", "lartesia_maksimale_e_kultivimit", "destinacioni_i_prodhimit", "forma_e_kultivimit", 
                "tipi_i_mbeshtetjes", "pastertia_variotore", "varieteti_kryesor", "perqindja_e_varietetit_kryesor", "varieteti_dytesor",
                "field_perqindja_e_varietetit_dytesor", "varietet_tjeter", "perqindja_e_varieteteve_te_tjere", "nenshartesa", 
                "shenime", "the_geom", "survejues" )
     
    
    exclude = [	   'surveyor'   ]
    
    list_filter = ['qarku','bashkia' ]
    search_fields=['qarku','bashkia','fshati']

    formfield_overrides = {
        
        gis_models.PointField: {"widget":  GoogleMapPointFieldWidget},
        gis_models.MultiPolygonField: {"widget":  GoogleMapPointFieldWidget},
        gis_models.PolygonField: {"widget":  GoogleMapPointFieldWidget}
    }
AdminSite.site.register(totalrowsvineyardalbania,totalrowsvineyardalbaniaAdmin)

class vineyardunitAdmin(LeafletGeoAdmin):
    
    
    # list_display=('id',"code",  'mapcode',	'blockcode','unitcode',"fshati", "bashkia", "qarku" ,
    #               'farmcode', 'fiscalcode', 'prevsoiltype', 'altitude', 'erosion' , 
    #             'soildepth', 'inclination',	'exposure',	'surface',	'cultivationtype',	'rowsdistance',	'plantsdistance' ,
    #             'couplesdistance', 'supportsystem',	'cultivationform',	'mincultivationheight',	'maxcultivationheight' ,
    #             'irrigationtype', 'mechanizationtype',	'varietypurity', 'principalvariety', 'secondaryvariety', 'othervariety' ,
    #             'notes', 'principalvarietyperc', 'secondaryvarietyperc', 'othervarietyperc', 'rowsdirection' , 
    #             'surveydate','surveyor' ,	'surveystate','surveycode',	'rootstocktype' ,
    #             'surveyor',	 'implantationyear', 'flag', 'area')
                
    #list_display=vineyardunit.objects.all()
    #   field_list = vineyardunit._meta.get_fields()
    #list_display = [field.name for field in field_list]
    fieldsets = [
        (
            None,
            {
                "classes": ["details"],
                "fields": ['mapcode',	'blockcode','unitcode',"code", "fshati", "bashkia", "qarku",'the_geom'],
            },
        ),
        (
            "Advanced options",
            {             
                "fields": ['farmcode', 'fiscalcode', 'prevsoiltype', 'altitude', 'erosion' , 
                'soildepth', 'inclination',	'exposure',	'surface',	'cultivationtype',	'rowsdistance',	'plantsdistance' ,
                'couplesdistance', 'supportsystem',	'cultivationform',	'mincultivationheight',	'maxcultivationheight' ,
                'irrigationtype', 'mechanizationtype',	'varietypurity', 'principalvariety', 'secondaryvariety', 'othervariety' ,
                'notes', 'principalvarietyperc', 'secondaryvarietyperc', 'othervarietyperc', 'rowsdirection' , 
                'surveydate', 	'surveystate','surveycode',	'rootstocktype' ,
                 'implantationyear', 'flag', 'area'],
                'classes': ['collapse',]
                
            },
        ),
    ]
    
    exclude = [	 'surveyor'   ]
    
    list_filter = ['qarku','bashkia' ]
    search_fields=['qarku','bashkia','fshati']

    formfield_overrides = {
        
        gis_models.PointField: {"widget":  GoogleMapPointFieldWidget},
        gis_models.MultiPolygonField: {"widget":  GoogleMapPointFieldWidget},
        gis_models.PolygonField: {"widget":  GoogleMapPointFieldWidget}
    }
AdminSite.site.register(vineyardunit,vineyardunitAdmin)
 
class bashkite_2014Admin(LeafletGeoAdmin):
 
    fieldsets = [
        (
            None,
            {
                "classes": ["details"],
                "fields": ["emer_bash", "qender_bash", "emer_qark", "qender_qark",'geom'],
            },
        ),
        (
            "Advanced options",
            {
                 
                 "fields": ['objectid','id_bash', 'id_qark', 
                 'pop_2011','pop_rgjcv','den_instat','sip','shape_area'],
                 'classes': ['collapse in',]
                
            },
        ),
    ]
    search_fields=['emer_qark','emer_bash'  ]

AdminSite.site.register(bashkite_2014,bashkite_2014Admin)

 
class breferencegridAdmin(LeafletGeoAdmin):
    list_display=('code','id','colnum','rownum' )
 
AdminSite.site.register(referencegrid,breferencegridAdmin)
 
#admin.site.register(vineyardunitproduction)
AdminSite.site.register(irrigationtype,DomainAdmin)
 
    
AdminSite.site.register(soiltype,DomainAdmin) 
AdminSite.site.register(rowsdirectiontype,DomainAdmin) 
AdminSite.site.register(exposure,DomainAdmin) 
AdminSite.site.register(rocktype,DomainAdmin)
class qarqetAdmin(LeafletGeoAdmin):
    list_display = ['objectid','id_qark','emer_qark','qend_qark'] 
    list_filter =list_display
    search_fields=list_display
AdminSite.site.register(qarqet,qarqetAdmin)
AdminSite.site.register(supporttype,DomainAdmin)

AdminSite.site.register(varietypurity,DomainAdmin)
 
AdminSite.site.register(cultivationtype,DomainAdmin)
AdminSite.site.register(user) 
 

AdminSite.site.register(rowsdirection,DomainAdmin) 
AdminSite.site.register(soildepth,DomainAdmin)
#LeafletGeoAdmin
class blockgridAdmin(LeafletGeoAdmin):
     list_display = ['code','rownum','colnum','mapcode']
     list_filter =('code','rownum','colnum','mapcode')
     search_fields=('code','rownum','colnum','mapcode')
     
AdminSite.site.register(blockgrid,blockgridAdmin) 

AdminSite.site.register(cultivationform,DomainAdmin)
       
class villagesAdmin(LeafletGeoAdmin):
    list_display = ['code','emri_zk','id_qark','emer_qark','qend_qark','id_bash','emer_bash',
                    'qend_bash','id_njqv','emer_njqv','emri_nga_tabela_village','id_rrethi','emer_rrethi'] 
    list_filter =['emer_qark','emer_rrethi']
    search_fields=['emer_qark','emer_rrethi','emer_njqv','code','emri_zk']
 
AdminSite.site.register(villages,villagesAdmin) 

AdminSite.site.register(variety,DomainAdmin)


class personAdmin(AdminSite.ModelAdmin):
    list_display = ['name','surname','fathername','secondname','birthdate','code','village',
                    'id','legal'] 
    list_filter =['name','surname','fathername' ]
    search_fields=['name','surname','fathername','village','code']
AdminSite.site.register(person,personAdmin)

AdminSite.site.register(surveystate,DomainAdmin)
 
AdminSite.site.register(productiontype,DomainAdmin)
AdminSite.site.register(inclination,DomainAdmin)
AdminSite.site.register(mechanizationtype,DomainAdmin)

AdminSite.site.register(rootstock,DomainAdmin)
