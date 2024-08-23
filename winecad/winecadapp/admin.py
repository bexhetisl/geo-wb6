from django.contrib import admin
from .models import vineyardunit
from django.db import models
from django.contrib.gis.db import models as gis_models
from mapwidgets.widgets import GoogleMapPointFieldWidget

class vineyardunitAdmin(admin.ModelAdmin):
    #list_display =('mapcode', 'blockcode','unitcode','farmcode','fiscalcode','geom_point')
    list_display =('mapcode', 'blockcode','unitcode','farmcode','fiscalcode','geom_point' )
    formfield_overrides = {
        gis_models.PointField: {"widget":  GoogleMapPointFieldWidget}
    }

admin.site.register(vineyardunit,vineyardunitAdmin)