from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

class vineyardunit(models.Model): 
#class vineyardunit(db):
    __tablename__ = 'vineyardunit'
    mapcode = models.CharField(max_length= 4)
    blockcode = models.CharField(max_length= 3)
    unitcode =models.IntegerField()
    farmcode = models.CharField(max_length= 20)
    fiscalcode = models.CharField(max_length= 20)
    geom_point = models.PointField(srid=4326)
    objects= models.Manager()
          # mapcode =db.CharField(max_length= 4)
    # blockcode =models.CharField(max_length= 3)
    # unitcode =models.IntegerField()
    # farmcode=models.CharField(max_length= 20)  # sipas video tutorial
    # fiscalcode=models.CharField(max_length= 20)  # sipas video tutorial
    # geom_polygon = db.PolygonField(srid=4326) 
    # geom_point = db.PointField(srid=4326)
    def __unicode__(self):
        return self.mapcode
    class Meta:
        verbose_name_plural="Vineyardunits"