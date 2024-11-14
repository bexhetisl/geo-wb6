# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models as db
from django.contrib.gis.db import  models as gis_models
from datetime import date
#from django_admin_geomap import GeoItem

class Location(db.Model):
    name = db.CharField(max_length=100)
    lon = db.FloatField()  # longitude
    lat = db.FloatField()  # latitude

#class bashkite_2014(db.Model,GeoItem):
class bashkite_2014(db.Model):
    objectid = db.IntegerField(blank=True, null=True)
    gid = db.IntegerField(blank=True, null=True)
    id_bash = db.IntegerField(unique=True, blank=True, null=True)
    emer_bash = db.CharField(max_length=100, blank=True, null=True)
    qender_bash = db.CharField(max_length=100, blank=True, null=True)
    id_qark = db.IntegerField(blank=True, null=True)
    emer_qark = db.CharField(max_length=100, blank=True, null=True)
    qender_qark = db.CharField(max_length=100, blank=True, null=True)
    pop_2011 = db.IntegerField(blank=True, null=True)
    pop_rgjcv = db.IntegerField(blank=True, null=True)
    den_instat = db.FloatField(blank=True, null=True)
    sip = db.FloatField(blank=True, null=True)
    shape_length = db.FloatField(blank=True, null=True)
    shape_area = db.FloatField(blank=True, null=True)
    geom = gis_models.MultiPolygonField(blank=True, null=True)
   # list_display = ['id_bash', 'emer_bash', ]
    objects = gis_models.Manager()
    class Meta:
        managed = False
        verbose_name_plural="bashkite_2014"
        db_table = 'bashkite_2014'
    def __str__(self)  :
        return self.emer_bash         
    # def __unicode__(self):
    #     return u'%s' % self.objects   
    # def __str__(self):
    #     return u'%s' % self.emer_bash
        
class qarqet(db.Model):
    objectid = db.IntegerField(blank=True, null=True)
    id_qark = db.IntegerField(unique=True, blank=True, null=True)
    emer_qark = db.CharField(max_length=100, blank=True, null=True)
    qend_qark = db.CharField(max_length=100, blank=True, null=True)
    shape_length = db.FloatField(blank=True, null=True)
    shape_area = db.FloatField(blank=True, null=True)
    geom = gis_models.MultiPolygonField(srid=32634, blank=True, null=True)

    class Meta:
        verbose_name_plural="qarqet"
        db_table = 'qarqet'
        ordering = ["id_qark","emer_qark"]
    def __str__(self)  :
        return self.emer_qark   
class villages(db.Model):
    objectid = db.IntegerField(blank=True, null=True)
    code = db.BigIntegerField(unique=True)
    emri_zk = db.CharField(max_length=60,blank=True,null=True)
    id_bash = db.CharField(max_length=50, blank=True, null=True)
    emer_bash = db.CharField(max_length=100, blank=True, null=True)
    qend_bash = db.CharField(max_length=100, blank=True, null=True)
    id_qark = db.CharField(max_length=50, blank=True, null=True)
    emer_qark = db.CharField(max_length=100, blank=True, null=True)
    qend_qark = db.CharField(max_length=100, blank=True, null=True)
    id_njqv = db.IntegerField(blank=True, null=True)
    emer_njqv = db.CharField(max_length=50, blank=True, null=True)
    emri_nga_tabela_village = db.CharField(max_length=50, blank=True, null=True)
    id_rrethi = db.IntegerField(blank=True, null=True)
    emer_rrethi = db.CharField(max_length=50, blank=True, null=True)
    shape_area = db.FloatField(blank=True, null=True)
    geom = gis_models.MultiPolygonField(blank=True, null=True)
    def __unicode__(self):
        return self.emri_zk
    # def __str__(self) -> str:
    #     return super().__str__()

    class Meta:
         db_table = "villages"
         verbose_name_plural="villages"
         ordering = ["emer_bash","emer_njqv"]
    def __str__(self)  :
        return self.emri_nga_tabela_village         
class variety(db.Model):
    code = db.AutoField(primary_key=True)
    description = db.CharField(max_length=80)
    registercode = db.CharField(max_length=20, blank=True, null=True, db_comment='Code used in the variety register, if any.')
    def __unicode__(self):
        return self.description
    class Meta:
         db_table = "variety"
         verbose_name_plural="variety"
    def __str__(self)  :
        return self.description
class person(db.Model):
    name = db.CharField(max_length=30)
    surname = db.CharField(max_length=30)
    secondname = db.CharField(max_length=30, blank=True, null=True)
    fathername = db.CharField(max_length=30, blank=True, null=True)
    birthdate = db.DateField()
    code = db.CharField(max_length=10, blank=True, null=True, db_comment='Code used only to identify surveyors')
    village = db.ForeignKey('Villages', db.DO_NOTHING, db_column='village', to_field='code', blank=True, null=True, db_comment='Village of residence.')
    legal = db.BooleanField(blank=True, null=True, db_comment='Is this a legal (as opposed to physical) person ?')
    id = db.AutoField(primary_key=True)

    def __unicode__(self):
        return self.name,self.fathername,self.surname
    class Meta:
        db_table = 'person'
        db_table_comment = 'A human being.'
        verbose_name_plural="persons"
    def __str__(self)  :
        return self.name + " " + self.fathername + " " + self.surname
class surveystate(db.Model):
    code = db.AutoField(primary_key=True)
    description = db.CharField(unique=True, max_length=80)
    def __unicode__(self):
        return self.description
    class Meta:
         db_table = 'surveystate'
         ordering = ["code","description"]
    def __str__(self)  :
        return self.description 
class productiontype(db.Model):
    code = db.AutoField(primary_key=True)
    description = db.CharField(max_length=80)
    def __unicode__(self):
        return self.description
    class Meta:
        #managed = False
        db_table = 'productiontype'
        ordering = ["code","description"]
    def __str__(self)  :
        return self.description 
class inclination(db.Model):
    code = db.AutoField(primary_key=True)
    description = db.CharField(max_length=80)
    def __unicode__(self):
        return self.description
    class Meta:
        #managed = False
        db_table = 'inclination'
        ordering = ["code","description"]
    def __str__(self)  :
        return self.description 
class mechanizationtype(db.Model):
    code = db.AutoField(primary_key=True)
    description = db.CharField(max_length=80)
    def __unicode__(self):
        return self.description
    class Meta:
         db_table = 'mechanizationtype'
         ordering = ["code","description"]        
    def __str__(self)  :
        return self.description 

        
class rowsdirection(db.Model):
    code = db.IntegerField(primary_key=True)
    description = db.CharField(max_length=80)
    def __unicode__(self):
        return self.description
    class Meta:
        db_table = 'rowsdirection'
        verbose_name="rowsdirection"
        ordering = ["code","description"]        
    def __str__(self)  :
        return self.description 
class soildepth(db.Model):
    code = db.AutoField(primary_key=True)
    description = db.CharField(max_length=80)
    def __unicode__(self):
        return self.description
    class Meta:
        verbose_name="soildepth"
        db_table = 'soildepth'
        ordering = ["code","description"]
    def __str__(self)  :
        return self.description 
class applog(db.Model):
    id = db.BigAutoField(primary_key=True)
    username = db.CharField(max_length=32)
    object = db.CharField(max_length=100, blank=True, null=True)
    time = db.DateTimeField()
    operation = db.CharField(max_length=10)
    objectid = db.IntegerField()
    objectpk = db.CharField(max_length=100, blank=True, null=True)
    tablename = db.CharField(max_length=100, blank=True, null=True)
    tableid = db.IntegerField(blank=True, null=True)
    def __unicode__(self):
        return self.description
    class Meta:
         verbose_name="applog"
         db_table = 'applog'
    def __str__(self)  :
        return self.description 
class blockgrid(db.Model):
    code = db.CharField(max_length=3, db_comment="Combination of row position as letters ('A' to 'J') and column position as numbers ('01' to '10')")
    rownum = db.IntegerField(blank=True, null=True, db_comment='Row number within the map sheet from the top')
    colnum = db.IntegerField(blank=True, null=True, db_comment='Column number within the map sheet from the leftmost.')
    the_geom = gis_models.PolygonField(blank=True, null=True)
    mapcode = db.CharField(max_length=4, blank=True, null=True, db_comment='Code of map sheet.')

    class Meta:
        verbose_name="blockgrid"
        db_table = 'blockgrid'
    def __str__(self)  :
        return self.mapcode 
  
         
class cultivationform(db.Model):
    code = db.AutoField(primary_key=True)
    description = db.CharField(max_length=80)
    class Meta:
        verbose_name_plural="cultivationform"
        db_table = 'cultivationform'
        ordering = ["code","description"]
    def __str__(self)  :
        return self.description 
class cultivationtype(db.Model):
    code = db.AutoField(primary_key=True)
    description = db.CharField(max_length=80)
    class Meta:
        verbose_name_plural="cultivationtype"
        db_table = 'cultivationtype'
        ordering = ["code","description"]        
    def __str__(self)  :
        return self.description 
        
class user(db.Model):
    title = db.CharField(max_length=50, blank=True, null=True)
    first_name = db.CharField(max_length=50, blank=True, null=True, db_comment='emri i deklaruesit')
    last_name = db.CharField(max_length=50, blank=True, null=True, db_comment='mbiemri i deklaruesit')
    email = db.CharField(unique=True, max_length=255, blank=True, null=True, db_comment='emaili zyrtar i deklaruesit.')
    password = db.CharField(max_length=255, blank=True, null=True)
    active = db.BooleanField(blank=True, null=True)
    confirmed_at = db.DateTimeField(blank=True, null=True)
    last_login_at = db.DateTimeField(blank=True, null=True)
    current_login_at = db.DateTimeField(blank=True, null=True)
    last_login_ip = db.CharField(max_length=25, blank=True, null=True)
    current_login_ip = db.CharField(max_length=25, blank=True, null=True)
    login_count = db.IntegerField(blank=True, null=True)
    fs_uniquifier = db.CharField(blank=True, null=True)

    class Meta:
        verbose_name_plural="user"
        db_table = 'user'
    def __str__(self)  :
        return self.first_name + " " + self.last_name 

class vaniardunittenant(db.Model):
    vineyardunit = db.OneToOneField('vineyardunit', db.DO_NOTHING, db_column='vineyardunit', primary_key=True)  # The composite primary key (vineyardunit, owner) found, that is not supported. The first column is selected.
    owner = db.ForeignKey(person, db.DO_NOTHING, db_column='owner')
    class Meta:
        verbose_name_plural = 'vaniard unit tenant'
        db_table = 'vaniardunittenant'
        unique_together = (('vineyardunit', 'owner'),)

class supporttype(db.Model):
    code = db.AutoField(primary_key=True)
    description = db.CharField(max_length=80)
    class Meta:
        verbose_name_plural="supporttype"
        db_table = 'supporttype'
        ordering = ["code","description"]
    def __str__(self)  :
        return self.description 
class varietypurity(db.Model):
    code = db.AutoField(primary_key=True)
    description = db.CharField(max_length=80)
    class Meta:
        verbose_name_plural="varietypurity"
        db_table = 'varietypurity'
        ordering = ["code","description"]
    def __str__(self)  :
        return self.description 

    
class exposure(db.Model):
    code = db.AutoField(primary_key=True)
    description = db.CharField(max_length=80)

    class Meta:
        verbose_name_plural="exposure"
        db_table = 'exposure'
        ordering = ["code","description"]       
    def __str__(self)  :
        return self.description 
class rocktype(db.Model):
    code = db.AutoField(primary_key=True)
    description = db.CharField(unique=True, max_length=80)

    class Meta:
        verbose_name_plural="rocktype"
        db_table = 'rocktype'
        ordering = ["code","description"]
    def __str__(self)  :
        return self.description 
class soiltype(db.Model):
    code = db.AutoField(primary_key=True)
    description = db.CharField(unique=True, max_length=80, blank=True, null=True)

    class Meta:
        verbose_name_plural="soiltype"
        db_table = 'soiltype'
        ordering = ["code","description"]
    def __str__(self)  :
        return self.description 
        
class rootstock(db.Model):
    code = db.AutoField(primary_key=True)
    description = db.CharField(unique=True, max_length=80, blank=True, null=True)

    class Meta:
        verbose_name_plural="rootstock"
        db_table = 'rootstock'
        ordering = ["code","description"]
    def __str__(self)  :
        return self.description 
        
class rowsdirectiontype(db.Model):
    code = db.AutoField(primary_key=True)
    description = db.CharField(max_length=80)

    class Meta:
        verbose_name_plural="rowsdirectiontype"
        db_table = 'rowsdirectiontype'
        ordering = ["code","description"]
    def __str__(self)  :
        return self.description 
        
class irrigationtype(db.Model):
    code = db.AutoField(primary_key=True)
    description = db.CharField(max_length=80)

    class Meta:
        verbose_name_plural="irrigationtype"
        db_table = 'irrigationtype'
        ordering = ["code","description"]
    def __str__(self)  :
        return self.description 
        
class referencegrid(db.Model):
    code = db.CharField(unique=True, max_length=4, db_comment="Combination of row position as letters (from 'A' to 'J') and column position as number.")
    the_geom = gis_models.PolygonField(blank=True, null=True)
    colnum = db.IntegerField(blank=True, null=True)
    rownum = db.IntegerField(blank=True, null=True)
    class Meta:
        verbose_name_plural="referencegrid"
        db_table = 'referencegrid'
    def __str__(self)  :
        return self.code 
 #list_display =('qarku','bashkia', 'fshati',	'mapcode',	'blockcode','unitcode','code',	'farmcode',	'fiscalcode','the_geom' )
class vineyardunit(db.Model):
 
    
    qarku = db.ForeignKey(qarqet, db.DO_NOTHING, db_column='qarku', to_field='id_qark', blank=True, null=True, db_comment='code of region')
    bashkia = db.ForeignKey(bashkite_2014, db.DO_NOTHING, db_column='bashkia', to_field='id_bash', blank=True, null=True, db_comment='code of municipality')
    fshati = db.ForeignKey(villages, db.DO_NOTHING, db_column='fshati', to_field='code', blank=True, null=True, db_comment='code of village')
    mapcode = db.CharField(max_length=4, db_comment='Code of map sheet as in the nation-wide grid.')
    blockcode = db.CharField(max_length=3, db_comment='Code of block within a map sheet.')
    farmcode = db.CharField(max_length=20, blank=True, null=True, db_comment="Code of unit's owner enterprise in the registry of farms.")
    fiscalcode = db.CharField(max_length=20, blank=True, null=True, db_comment="Tax code of the unit's owner.")
    prevsoiltype = db.ForeignKey(soiltype, db.DO_NOTHING, db_column='prevsoiltype', blank=True, null=True, db_comment='Prevalent soil type on which the unit is located.')
    altitude = db.IntegerField(blank=True, null=True, db_comment='Altitude of parcle in meters')
    erosion = db.BooleanField(blank=True, null=True, db_comment='Presence of erosion.')
    soildepth = db.ForeignKey(soildepth, db.DO_NOTHING, db_column='soildepth', blank=True, null=True, db_comment='Class of soil depth.')
    inclination = db.ForeignKey(inclination, db.DO_NOTHING, db_column='inclination', blank=True, null=True, db_comment='Class of inclination.')
    exposure = db.ForeignKey(exposure, db.DO_NOTHING, db_column='exposure', blank=True, null=True, db_comment='Facing of vineyard unit.')
    surface = db.FloatField(blank=True, null=True, db_comment='Surface of unit in square meters.')
    cultivationtype = db.ForeignKey(cultivationtype, db.DO_NOTHING, db_column='cultivationtype', blank=True, null=True, db_comment='Cultivation type  and relation to other crop/orchard types.')
    rowsdistance = db.FloatField(blank=True, null=True, db_comment='Distance in centimeters between rows of plants.')
    plantsdistance = db.FloatField(blank=True, null=True, db_comment='Distance in centimeters between plsnts belonging to the same row.')
    couplesdistance = db.FloatField(blank=True, null=True, db_comment='Distance in centimeters between plants planted in couples.')
    supportsystem = db.ForeignKey(supporttype, db.DO_NOTHING, db_column='supportsystem', blank=True, null=True, db_comment='Plant support system type.')
    cultivationform = db.ForeignKey(cultivationform, db.DO_NOTHING, db_column='cultivationform', blank=True, null=True, db_comment='Form of cultivation and pruning.')
    mincultivationheight = db.FloatField(blank=True, null=True, db_comment='Minimum cultivation height in centimeters.')
    maxcultivationheight = db.FloatField(blank=True, null=True, db_comment='Maximum cultivation height in centimeters.')
    irrigationtype = db.ForeignKey(irrigationtype, db.DO_NOTHING, db_column='irrigationtype', blank=True, null=True, db_comment='Type of irrigation (left empty if non-irrigated).')
    mechanizationtype = db.ForeignKey(mechanizationtype, db.DO_NOTHING, db_column='mechanizationtype', blank=True, null=True, db_comment='Type of vineyard unit mechanization.')
    varietypurity = db.ForeignKey(varietypurity, db.DO_NOTHING, db_column='varietypurity', blank=True, null=True, db_comment='Grade of purity of the grape variety.')
    principalvariety = db.ForeignKey(variety, db.DO_NOTHING, db_column='principalvariety', blank=True, null=True, db_comment='Type of principal variety.')
    secondaryvariety = db.ForeignKey(variety, db.DO_NOTHING, db_column='secondaryvariety', related_name='vineyardunit_secondaryvariety_set', blank=True, null=True, db_comment='Type of secondary grape variety.')
    othervariety = db.ForeignKey(variety, db.DO_NOTHING, db_column='othervariety', related_name='vineyardunit_othervariety_set', blank=True, null=True, db_comment='Type of other grape variety.')
    notes = db.TextField(blank=True, null=True, db_comment='Type of other grape variety.')
    principalvarietyperc = db.IntegerField(blank=True, null=True, db_comment='Percentage of plant of the principal grape variety.')
    secondaryvarietyperc = db.IntegerField(blank=True, null=True, db_comment='Percentage of plant of the secondary grape variety.')
    othervarietyperc = db.IntegerField(blank=True, null=True, db_comment='Percentage of plants of the other grape variety.')
    rowsdirection = db.ForeignKey(rowsdirection, db.DO_NOTHING, db_column='rowsdirection', blank=True, null=True, db_comment='General direction of rows')
    surveydate = db.DateField(blank=True, default=date.today,null=True, db_comment='Date of survey.')
   
    surveystate = db.ForeignKey(surveystate, db.DO_NOTHING, db_column='surveystate', blank=True, null=True, db_comment='State of vineyard unit in survey.')
    unitcode = db.IntegerField(blank=True, null=True, db_comment='Unique code of vineyard unit within the block.')
    surveycode = db.CharField(max_length=30, blank=True, null=True, db_comment='Code used during the survey to identify the vineyard unit.')
    rootstocktype = db.ForeignKey(rootstock, db.DO_NOTHING, db_column='rootstocktype', blank=True, null=True)
    #surveyor = db.ForeignKey(person, db.DO_NOTHING, db_column='surveyor', blank=True, null=True,  default=None)
    surveyor = db.ForeignKey(person, db.DO_NOTHING, db_column='surveyor', blank=True, null=True,  default=None)
    implantationyear = db.IntegerField(blank=True, null=True, db_comment='Year of vineyard implantation')
    code = db.CharField(max_length=20, blank=True, null=True)
    flag = db.IntegerField(blank=True, null=True)
    area = db.IntegerField(blank=True, null=True, db_comment='area of polygon')
    the_geom = gis_models.PolygonField(blank=True, null=True, db_comment='Geometry of the vineyard unit (a polygon)')
    
   
    def __unicode__(self):
        return self.emri_zk
    class Meta:
         db_table = "vineyardunit"
         verbose_name_plural="vineyardunit"
         unique_together = (('mapcode', 'blockcode', 'unitcode'),)
         ordering = ["qarku","bashkia","fshati","id" ]
class vineyardunitowner(db.Model):
    vineyardunit = db.ForeignKey(vineyardunit,   on_delete=db.CASCADE, db_column='vineyardunit')
    owner = db.OneToOneField(person, db.DO_NOTHING, db_column='owner', primary_key=True)  # The composite primary key (owner, vineyardunit) found, that is not supported. The first column is selected.
    def __unicode__(self):
        return self.vineyardunit
    class Meta:
        db_table = 'vineyardunitowner'
        verbose_name_plural="vineyardunitowner"
        unique_together = (('owner', 'vineyardunit'),)
class vineyardunittenant(db.Model):
    vineyardunit = db.OneToOneField(vineyardunit, on_delete=db.CASCADE, db_column='vineyardunit', primary_key=True)  # The composite primary key (vineyardunit, tenant) found, that is not supported. The first column is selected.
    tenant = db.ForeignKey(person, db.DO_NOTHING, db_column='tenant')
    class Meta:
        verbose_name_plural="vineyardunittenant"
        db_table = 'vineyardunittenant'
        unique_together = (('vineyardunit', 'tenant'),)
class vineyardunitrocktype(db.Model):
    vineyardunit = db.OneToOneField(vineyardunit, db.DO_NOTHING, db_column='vineyardunit', primary_key=True)  # The composite primary key (vineyardunit, rocktype) found, that is not supported. The first column is selected.
    rocktype = db.ForeignKey(rocktype, db.DO_NOTHING, db_column='rocktype')
    class Meta:
        verbose_name_plural="vineyardunitrocktype"
        db_table = 'vineyardunitrocktype'
        unique_together = (('vineyardunit', 'rocktype'),)
              
class vineyardunitproduction(db.Model):
    vineyardunit = db.OneToOneField(vineyardunit, db.DO_NOTHING, db_column='vineyardunit', primary_key=True)  # The composite primary key (vineyardunit, productiontype) found, that is not supported. The first column is selected.
    productiontype = db.ForeignKey(productiontype, db.DO_NOTHING, db_column='productiontype')
    class Meta:
        verbose_name_plural="vineyardunitproduction"
        db_table = 'vineyardunitproduction'
        unique_together = (('vineyardunit', 'productiontype'),)
        
class vineyardunitsoiltype(db.Model):
    vineyardunit = db.OneToOneField(vineyardunit, db.DO_NOTHING, db_column='vineyardunit', primary_key=True)  # The composite primary key (vineyardunit, soiltype) found, that is not supported. The first column is selected.
    soiltype = db.ForeignKey(soiltype, db.DO_NOTHING, db_column='soiltype')
    type = db.IntegerField(blank=True, null=True, db_comment='Type of soil type for vineyarsd unit: 1 prmary: 2 secondary.')
    class Meta:
        verbose_name_plural="vineyardunitsoiltype"
        db_table = 'vineyardunitsoiltype'
        unique_together = (('vineyardunit', 'soiltype'),)
        
class totalrowsvineyardalbania(db.Model):
    id = db.IntegerField(primary_key=True)
    qarku = db.CharField(db_column='Qarku', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bashkia = db.CharField(db_column='Bashkia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fshati = db.CharField(db_column='Fshati', max_length=60, blank=True, null=True)  # Field name made lowercase.
    kodi_i_hartes = db.CharField(db_column='Kodi i Hartes', max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    blloku = db.CharField(db_column='Blloku', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kodiparceles = db.IntegerField(blank=True, null=True)
    pronari = db.TextField(db_column='Pronari', blank=True, null=True)  # Field name made lowercase.
    perdoruesi = db.TextField(db_column='Perdoruesi', blank=True, null=True)  # Field name made lowercase.
    kodi_i_fermes = db.CharField(db_column='Kodi i Fermes', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kodi_fiskal = db.CharField(db_column='Kodi Fiskal', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gjendja_e_vreshtit = db.CharField(db_column='Gjendja e vreshtit', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_e_vrojtimit = db.TextField(db_column='Data e vrojtimit', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    latesia_nga_deti = db.IntegerField(db_column='Latesia nga deti', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    erozioni = db.BooleanField(db_column='Erozioni', blank=True, null=True)  # Field name made lowercase.
    siperfaqja = db.FloatField(db_column='Siperfaqja', blank=True, null=True)  # Field name made lowercase.
    siperfaqja_ne_ha = db.FloatField(db_column='Siperfaqja ne HA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    siperfaqja_faktike = db.IntegerField(db_column='Siperfaqja faktike', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    viti_i_mbjelljes = db.IntegerField(db_column='Viti i mbjelljes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distanca_midis_rreshtave = db.FloatField(db_column='Distanca midis rreshtave', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distanca_midis_bimeve = db.FloatField(db_column='Distanca midis bimeve', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distanca_midis_cifteve = db.FloatField(db_column='Distanca midis cifteve', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lloji_i_ujitjes = db.CharField(db_column='Lloji i ujitjes', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pjerresia = db.CharField(db_column='Pjerresia', max_length=80, blank=True, null=True)  # Field name made lowercase.
    mekanizimi = db.CharField(db_column='Mekanizimi', max_length=80, blank=True, null=True)  # Field name made lowercase.
    drejtimi_i_rreshtave = db.CharField(db_column='Drejtimi i Rreshtave', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ekspozimi = db.CharField(db_column='Ekspozimi', max_length=80, blank=True, null=True)  # Field name made lowercase.
    tipi_i_kultivimit = db.CharField(db_column='Tipi i kultivimit', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thellesi_e_tokes = db.CharField(db_column='Thellesi e Tokes', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tipi_i_tokes_meparshme = db.CharField(db_column='Tipi i tokes meparshme', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shkembi_amnor = db.TextField(db_column='Shkembi amnor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tipi_i_tokes = db.TextField(db_column='Tipi i tokes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lartesia_mumimale_e_kultivimit = db.FloatField(db_column='Lartesia mumimale e Kultivimit', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lartesia_maksimale_e_kultivimit = db.FloatField(db_column='Lartesia maksimale e Kultivimit', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    destinacioni_i_prodhimit = db.TextField(db_column='Destinacioni i prodhimit', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    forma_e_kultivimit = db.CharField(db_column='Forma e Kultivimit', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tipi_i_mbeshtetjes = db.CharField(db_column='Tipi i mbeshtetjes', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pastertia_variotore = db.CharField(db_column='Pastertia variotore', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    varieteti_kryesor = db.CharField(db_column='Varieteti kryesor', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    perqindja_e_varietetit_kryesor = db.IntegerField(db_column='Perqindja e varietetit kryesor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    varieteti_dytesor = db.CharField(db_column='Varieteti dytesor', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_perqindja_e_varietetit_dytesor = db.IntegerField(db_column=' Perqindja e varietetit dytesor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    varietet_tjeter = db.CharField(db_column='Varietet tjeter', max_length=80, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    perqindja_e_varieteteve_te_tjere= db.IntegerField(db_column='Perqindja e varieteteve te tjere', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nenshartesa = db.CharField(db_column='Nenshartesa', max_length=80, blank=True, null=True)  # Field name made lowercase.
    shenime = db.TextField(db_column='Shenime', blank=True, null=True)  # Field name made lowercase.
    the_geom = gis_models.PolygonField(blank=True, null=True)
    survejues = db.TextField(db_column='Survejues', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'total_rows_vineyard_albania'

 