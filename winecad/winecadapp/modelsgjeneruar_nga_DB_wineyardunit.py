# -*- coding: utf-8 -*-
from django.contrib.gis.db import models
class Aaa222(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    objectid = models.IntegerField(blank=True, null=True)
    gid = models.IntegerField(blank=True, null=True)
    id_bash = models.IntegerField(blank=True, null=True)
    emer_bash = models.CharField(max_length=100, blank=True, null=True)
    qender_bash = models.CharField(max_length=100, blank=True, null=True)
    id_qark = models.IntegerField(blank=True, null=True)
    emer_qark = models.CharField(max_length=100, blank=True, null=True)
    qender_qark = models.CharField(max_length=100, blank=True, null=True)
    pop_2011 = models.IntegerField(blank=True, null=True)
    pop_rgjcv = models.IntegerField(blank=True, null=True)
    den_instat = models.FloatField(blank=True, null=True)
    sip = models.FloatField(blank=True, null=True)
    shape_length = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'aaa222'
class Addr(models.Model):
    gid = models.AutoField(primary_key=True)
    tlid = models.BigIntegerField(blank=True, null=True)
    fromhn = models.CharField(max_length=12, blank=True, null=True)
    tohn = models.CharField(max_length=12, blank=True, null=True)
    side = models.CharField(max_length=1, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)
    plus4 = models.CharField(max_length=4, blank=True, null=True)
    fromtyp = models.CharField(max_length=1, blank=True, null=True)
    totyp = models.CharField(max_length=1, blank=True, null=True)
    fromarmid = models.IntegerField(blank=True, null=True)
    toarmid = models.IntegerField(blank=True, null=True)
    arid = models.CharField(max_length=22, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'addr'
class Addrfeat(models.Model):
    gid = models.AutoField(primary_key=True)
    tlid = models.BigIntegerField(blank=True, null=True)
    statefp = models.CharField(max_length=2)
    aridl = models.CharField(max_length=22, blank=True, null=True)
    aridr = models.CharField(max_length=22, blank=True, null=True)
    linearid = models.CharField(max_length=22, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    lfromhn = models.CharField(max_length=12, blank=True, null=True)
    ltohn = models.CharField(max_length=12, blank=True, null=True)
    rfromhn = models.CharField(max_length=12, blank=True, null=True)
    rtohn = models.CharField(max_length=12, blank=True, null=True)
    zipl = models.CharField(max_length=5, blank=True, null=True)
    zipr = models.CharField(max_length=5, blank=True, null=True)
    edge_mtfcc = models.CharField(max_length=5, blank=True, null=True)
    parityl = models.CharField(max_length=1, blank=True, null=True)
    parityr = models.CharField(max_length=1, blank=True, null=True)
    plus4l = models.CharField(max_length=4, blank=True, null=True)
    plus4r = models.CharField(max_length=4, blank=True, null=True)
    lfromtyp = models.CharField(max_length=1, blank=True, null=True)
    ltotyp = models.CharField(max_length=1, blank=True, null=True)
    rfromtyp = models.CharField(max_length=1, blank=True, null=True)
    rtotyp = models.CharField(max_length=1, blank=True, null=True)
    offsetl = models.CharField(max_length=1, blank=True, null=True)
    offsetr = models.CharField(max_length=1, blank=True, null=True)
    the_geom = models.LineStringField(srid=4269, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'addrfeat'
class Applog(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=32)
    object = models.CharField(max_length=100, blank=True, null=True)
    time = models.DateTimeField()
    operation = models.CharField(max_length=10)
    objectid = models.IntegerField()
    objectpk = models.CharField(max_length=100, blank=True, null=True)
    tablename = models.CharField(max_length=100, blank=True, null=True)
    tableid = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'applog'
        db_table_comment = 'Log of application user transactions.'
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)
    class Meta:
        managed = False
        db_table = 'auth_group'
class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)
class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)
class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'
class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)
class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)
class Bashkite2014(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    gid = models.IntegerField(blank=True, null=True)
    id_bash = models.IntegerField(unique=True, blank=True, null=True)
    emer_bash = models.CharField(max_length=100, blank=True, null=True)
    qender_bash = models.CharField(max_length=100, blank=True, null=True)
    id_qark = models.IntegerField(blank=True, null=True)
    emer_qark = models.CharField(max_length=100, blank=True, null=True)
    qender_qark = models.CharField(max_length=100, blank=True, null=True)
    pop_2011 = models.IntegerField(blank=True, null=True)
    pop_rgjcv = models.IntegerField(blank=True, null=True)
    den_instat = models.FloatField(blank=True, null=True)
    sip = models.FloatField(blank=True, null=True)
    shape_length = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bashkite_2014'


class Bg(models.Model):
    gid = models.AutoField()
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    blkgrpce = models.CharField(max_length=1, blank=True, null=True)
    bg_id = models.CharField(primary_key=True, max_length=12)
    namelsad = models.CharField(max_length=13, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bg'
        db_table_comment = 'block groups'


class Blockgrid(models.Model):
    code = models.CharField(max_length=3, db_comment="Combination of row position as letters ('A' to 'J') and column position as numbers ('01' to '10')")
    rownum = models.IntegerField(blank=True, null=True, db_comment='Row number within the map sheet from the top')
    colnum = models.IntegerField(blank=True, null=True, db_comment='Column number within the map sheet from the leftmost.')
    the_geom = models.PolygonField(blank=True, null=True)
    mapcode = models.CharField(max_length=4, blank=True, null=True, db_comment='Code of map sheet.')

    class Meta:
        managed = False
        db_table = 'blockgrid'
        db_table_comment = 'Grid of blocks within reference maps.'


class Cilesia(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cilesia'
        db_table_comment = 'Domain per cilesine e veres'
class County(models.Model):
    gid = models.AutoField(unique=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    countyns = models.CharField(max_length=8, blank=True, null=True)
    cntyidfp = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=100, blank=True, null=True)
    namelsad = models.CharField(max_length=100, blank=True, null=True)
    lsad = models.CharField(max_length=2, blank=True, null=True)
    classfp = models.CharField(max_length=2, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    csafp = models.CharField(max_length=3, blank=True, null=True)
    cbsafp = models.CharField(max_length=5, blank=True, null=True)
    metdivfp = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.BigIntegerField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'county'


class CountyLookup(models.Model):
    st_code = models.IntegerField(primary_key=True)  # The composite primary key (st_code, co_code) found, that is not supported. The first column is selected.
    state = models.CharField(max_length=2, blank=True, null=True)
    co_code = models.IntegerField()
    name = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'county_lookup'
        unique_together = (('st_code', 'co_code'),)


class CountysubLookup(models.Model):
    st_code = models.IntegerField(primary_key=True)  # The composite primary key (st_code, co_code, cs_code) found, that is not supported. The first column is selected.
    state = models.CharField(max_length=2, blank=True, null=True)
    co_code = models.IntegerField()
    county = models.CharField(max_length=90, blank=True, null=True)
    cs_code = models.IntegerField()
    name = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countysub_lookup'
        unique_together = (('st_code', 'co_code', 'cs_code'),)


class Cousub(models.Model):
    gid = models.AutoField(unique=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    cousubfp = models.CharField(max_length=5, blank=True, null=True)
    cousubns = models.CharField(max_length=8, blank=True, null=True)
    cosbidfp = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100, blank=True, null=True)
    namelsad = models.CharField(max_length=100, blank=True, null=True)
    lsad = models.CharField(max_length=2, blank=True, null=True)
    classfp = models.CharField(max_length=2, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    cnectafp = models.CharField(max_length=3, blank=True, null=True)
    nectafp = models.CharField(max_length=5, blank=True, null=True)
    nctadvfp = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.DecimalField(max_digits=14, decimal_places=0, blank=True, null=True)
    awater = models.DecimalField(max_digits=14, decimal_places=0, blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cousub'


class Cultivationform(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'cultivationform'
        db_table_comment = 'Form of cultivation and pruning nomenclature (Goblet, Sheshi-type pruning, etc.)'


class Cultivationtype(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'cultivationtype'
        db_table_comment = 'Cultivation type nomenclature (Pure cultivation, In association with olive trees, etc.'


class Deklarataeprodhimit(models.Model):
    id = models.BigAutoField(primary_key=True)
    viti_i_veres = models.IntegerField(blank=True, null=True, db_comment='viti i prodhimit te veres')
    kategori_lenda_e_pare = models.ForeignKey('KategoriLendaEPare', models.DO_NOTHING, db_column='kategori_lenda_e_pare', db_comment='Kategoria e produkteve nga δshtδ prodhuar vera ( rrush, musht, verδ e re nδ fermentim)')
    nipt_furnizuesi = models.CharField(max_length=50, blank=True, null=True, db_comment='NIUS/NIPT i furnizuesit (nδ rast prodhimi vetjak shδno PV, dhe mos shδno origjinδn)')
    origjina = models.ForeignKey('Origjina', models.DO_NOTHING, db_column='origjina', db_comment='origjina Shqipδri/Jashtδ Shqipδrisδ')
    vere_e_prodhuar_b = models.FloatField(blank=True, null=True, db_comment='Verδ e prodhuar (hL) (B) ')
    vere_e_prodhuar_k_ro = models.FloatField(blank=True, null=True, db_comment='Verδ e prodhuar (hL) K/Ro')
    musht_gjendje_b = models.FloatField(blank=True, null=True, db_comment='Musht (hL) B nδ gjendje ne datδn e deklarimit(hektoliter)')
    musht_gjendje_k_ro = models.FloatField(blank=True, null=True, db_comment='Musht (hL)K/Ro nδ gjendje ne datδn e deklarimit(hektoliter)')
    vere_fermentim_b = models.FloatField(blank=True, null=True, db_comment='vere  e re (hL)B  ne fermentim ne datδn e deklarimit(hektoliter)')
    vere_fermentim_k_ro = models.FloatField(blank=True, null=True, db_comment='vere  e re  (hL)K/Ro  ne fermentim ne datδn e deklarimit(hektoliter)')
    cilesia = models.ForeignKey('EomtgjmProdhim', models.DO_NOTHING, db_column='cilesia', blank=True, null=True, db_comment='Cilδsia (EOM - TGJM -verδ varietore pa EOM/TGJM - verδ  pa EOM/TGJM)')
    totali = models.FloatField(blank=True, null=True, db_comment='Totali (hL)')
    data_e_deklarimit = models.DateField(blank=True, null=True, db_comment='data e deklarimit/nenshkrimit')
    verejtje_shenime = models.CharField(max_length=255, blank=True, null=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', db_comment='id e deklaruesit(merret nga tabela deklarues)')
    emri_nderrmarjes = models.CharField(max_length=255, blank=True, null=True)
    vendi_magazinimit = models.CharField(max_length=255, blank=True, null=True)
    nipt = models.CharField(max_length=35, blank=True, null=True)
    email = models.CharField(max_length=75, blank=True, null=True)
    telefon = models.CharField(max_length=35, blank=True, null=True)
    user_comments = models.CharField(max_length=255, blank=True, null=True)
    controller_comments = models.CharField(max_length=255, blank=True, null=True)
    statusi = models.ForeignKey('Status', models.DO_NOTHING, db_column='statusi', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deklarataeprodhimit'
        db_table_comment = ' deklarimi i vlerave  te veres/mushtit'


class Deklarataestoqeve(models.Model):
    id = models.BigAutoField(primary_key=True)
    viti_i_veres = models.IntegerField(blank=True, null=True)
    kategoria_e_produktit = models.ForeignKey('KategoriaEProduktit', models.DO_NOTHING, db_column='kategoria_e_produktit')
    mbajtesi_stokut = models.ForeignKey('MbajtesiStokut', models.DO_NOTHING, db_column='mbajtesi_stokut', blank=True, null=True)
    cilesia = models.ForeignKey(Cilesia, models.DO_NOTHING, db_column='cilesia', blank=True, null=True)
    origjina = models.ForeignKey('Origjina', models.DO_NOTHING, db_column='origjina')
    lloj_mushti = models.ForeignKey('LlojMushti', models.DO_NOTHING, db_column='lloj_mushti', blank=True, null=True)
    sasia_badhe = models.FloatField(blank=True, null=True)
    sasia_kuqeroze = models.FloatField(blank=True, null=True)
    sasia_bardh_kuqeroz = models.FloatField(blank=True, null=True)
    sasia_total = models.FloatField(blank=True, null=True)
    grand_total = models.FloatField(blank=True, null=True)
    data_e_deklarimit = models.DateField(blank=True, null=True)
    verejtje_shenime = models.CharField(max_length=255, blank=True, null=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid')
    emri_nderrmarjes = models.CharField(max_length=255, blank=True, null=True)
    vendi_magazinimit = models.CharField(max_length=255, blank=True, null=True)
    nipt = models.CharField(max_length=35, blank=True, null=True)
    email = models.CharField(max_length=75, blank=True, null=True)
    telefon = models.CharField(max_length=35, blank=True, null=True)
    user_comments = models.CharField(max_length=255, blank=True, null=True)
    controller_comments = models.CharField(max_length=255, blank=True, null=True)
    statusi = models.ForeignKey('Status', models.DO_NOTHING, db_column='statusi', blank=True, null=True)
    lloj_tjeter = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deklarataestoqeve'


class Deklarataevjeljes(models.Model):
    id = models.BigAutoField(primary_key=True)
    viti_i_veres = models.IntegerField(blank=True, null=True, db_comment='viti i veres')
    rrush_i_vlefshem_per = models.ForeignKey('RrushIVlefshemPer', models.DO_NOTHING, db_column='rrush_i_vlefshem_per', db_comment='Rrush i vlefshδm pδr verδ:  EOM, TGJM, Varietore ose thjeshtδ Verδ specifiko)')
    siperfaqja_prodhim = models.FloatField(blank=True, null=True, db_comment='siperfaqja ne Ha')
    nr_vreshtit = models.CharField(max_length=25, blank=True, null=True, db_comment='nr I vreshtit (code=Harte+bllok+parcele)')
    ibardh100kg = models.FloatField(blank=True, null=True, db_comment='sasia rrush I bardh ne njesi 100 kg')
    izikuq100kg = models.FloatField(blank=True, null=True, db_comment='totali ne njesi 100 kg')
    totali100kg = models.FloatField(blank=True, null=True, db_comment='totali ne njesi 100 kg')
    derguar_ne_kantinen_vetjake = models.FloatField(blank=True, null=True, db_comment='sasia derguar ne kantinen vetjake rrush njesi 100kg')
    destinacion1_emri = models.CharField(max_length=100, blank=True, null=True, db_comment='emri i destinacionit tjeter(1)')
    d1_rrush100kg = models.FloatField(blank=True, null=True, db_comment='sasia e njesive 100kg te rushit derguar ne destinacion tjeter 1')
    d1_musht100hl = models.FloatField(blank=True, null=True, db_comment='sasia e njesive 100kg te mushtit derguar ne destinacion tjeter 1')
    vere100_shitur_p1 = models.FloatField(blank=True, null=True, db_comment='vere njesi 100kg shitur prodhuesit te veres 1')
    musht100_shitur_p1 = models.FloatField(blank=True, null=True, db_comment='musht njesi 100kg shitur prodhuesit te veres 1')
    nipt_p1 = models.CharField(max_length=50, blank=True, null=True, db_comment='nipti i prodhuesit 1,nese bleresi eshte prodhues')
    data_e_deklarimit = models.DateField(blank=True, null=True, db_comment='data e deklarimit/nenshkrimit')
    verejtje_shenime = models.CharField(max_length=255, blank=True, null=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', db_comment='id e deklaruesit(merret nga tabela deklarues)')
    emri_nderrmarjes = models.CharField(max_length=255, blank=True, null=True)
    vendi_magazinimit = models.CharField(max_length=255, blank=True, null=True)
    nipt = models.CharField(max_length=35, blank=True, null=True)
    email = models.CharField(max_length=75, blank=True, null=True)
    telefon = models.CharField(max_length=35, blank=True, null=True)
    user_comments = models.CharField(max_length=255, blank=True, null=True)
    controller_comments = models.CharField(max_length=255, blank=True, null=True)
    statusi = models.ForeignKey('Status', models.DO_NOTHING, db_column='statusi', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deklarataevjeljes'


class Deklarues(models.Model):
    id = models.BigAutoField(primary_key=True)
    tip_kerkese = models.ForeignKey('TipKerkese', models.DO_NOTHING, db_column='tip_kerkese', blank=True, null=True, db_comment='vlerat e tipit te kerkeses zgjidhen nga domain(tabela) tip_kerkese.')
    emri = models.CharField(max_length=75, blank=True, null=True, db_comment='emri i deklaruesit')
    atesia = models.CharField(max_length=35, blank=True, null=True, db_comment='atesia e deklaruesit')
    mbiemri = models.CharField(max_length=35, blank=True, null=True, db_comment='mbiemri i deklaruesit')
    person_fizik_juridik = models.ForeignKey('PersonFizikJuridik', models.DO_NOTHING, db_column='person_fizik_juridik', blank=True, null=True, db_comment='tipi i personit qe ben vetdeklarimin(fizik ose juridik), vlerat ne domain person_fizik_juridik')
    fiscalcode = models.CharField(max_length=20, blank=True, null=True, db_comment='kodi fiskal qe mund te jete per kompanine ose personin (NIPT)')
    datelindja = models.DateField(blank=True, null=True, db_comment='data e lindjes se deklaruesit.')
    pozicioni_punes = models.ForeignKey('PozicioniPunes', models.DO_NOTHING, db_column='pozicioni_punes', blank=True, null=True)
    email_zyrtar = models.CharField(max_length=50, blank=True, null=True, db_comment='emaili zyrtar i deklaruesit.')
    adresa_private = models.CharField(max_length=255, blank=True, null=True, db_comment='adresa private e deklaruesit')
    kodi_postar = models.CharField(max_length=35, blank=True, null=True, db_comment='kodi postar i deklaruesit')
    qarku = models.ForeignKey('Qarqet', models.DO_NOTHING, db_column='qarku', to_field='id_qark', blank=True, null=True, db_comment='qarku i adreses se deklaruesit.')
    bashkia = models.ForeignKey(Bashkite2014, models.DO_NOTHING, db_column='bashkia', to_field='id_bash', blank=True, null=True, db_comment='bashkia e adreses se deklaruesit.')
    telefon = models.CharField(max_length=35, blank=True, null=True, db_comment='nr i telefonit te deklarusit')
    adresa_punes = models.CharField(max_length=255, blank=True, null=True, db_comment='adresa e punes, vreshtit, kantines nese eshte e ndryshme nga adresa private')
    date_deklarimi = models.DateField(blank=True, null=True, db_comment='data e deklarimit  te te dhenave')
    publication_date = models.DateField(blank=True, null=True)
    publication_update = models.DateField(blank=True, null=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    user_comments = models.CharField(max_length=255, blank=True, null=True)
    controller_comments = models.CharField(max_length=255, blank=True, null=True)
    statusi = models.ForeignKey('Userstatus', models.DO_NOTHING, db_column='statusi', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deklarues'


class DirectionLookup(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    abbrev = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direction_lookup'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Edges(models.Model):
    gid = models.AutoField(primary_key=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tlid = models.BigIntegerField(blank=True, null=True)
    tfidl = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tfidr = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    smid = models.CharField(max_length=22, blank=True, null=True)
    lfromadd = models.CharField(max_length=12, blank=True, null=True)
    ltoadd = models.CharField(max_length=12, blank=True, null=True)
    rfromadd = models.CharField(max_length=12, blank=True, null=True)
    rtoadd = models.CharField(max_length=12, blank=True, null=True)
    zipl = models.CharField(max_length=5, blank=True, null=True)
    zipr = models.CharField(max_length=5, blank=True, null=True)
    featcat = models.CharField(max_length=1, blank=True, null=True)
    hydroflg = models.CharField(max_length=1, blank=True, null=True)
    railflg = models.CharField(max_length=1, blank=True, null=True)
    roadflg = models.CharField(max_length=1, blank=True, null=True)
    olfflg = models.CharField(max_length=1, blank=True, null=True)
    passflg = models.CharField(max_length=1, blank=True, null=True)
    divroad = models.CharField(max_length=1, blank=True, null=True)
    exttyp = models.CharField(max_length=1, blank=True, null=True)
    ttyp = models.CharField(max_length=1, blank=True, null=True)
    deckedroad = models.CharField(max_length=1, blank=True, null=True)
    artpath = models.CharField(max_length=1, blank=True, null=True)
    persist = models.CharField(max_length=1, blank=True, null=True)
    gcseflg = models.CharField(max_length=1, blank=True, null=True)
    offsetl = models.CharField(max_length=1, blank=True, null=True)
    offsetr = models.CharField(max_length=1, blank=True, null=True)
    tnidf = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    tnidt = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    the_geom = models.MultiLineStringField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edges'


class Eomtgjm(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'eomtgjm'
        db_table_comment = 'vresht me EOM, TGJM '


class EomtgjmProdhim(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'eomtgjm_prodhim'
        db_table_comment = 'Domain per cilesine e veres: me EOM, Pa EOM etj'


class Exposure(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'exposure'
        db_table_comment = 'Exposure nomenclature (North, North-East, etc.)'


class Faces(models.Model):
    gid = models.AutoField(primary_key=True)
    tfid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    statefp00 = models.CharField(max_length=2, blank=True, null=True)
    countyfp00 = models.CharField(max_length=3, blank=True, null=True)
    tractce00 = models.CharField(max_length=6, blank=True, null=True)
    blkgrpce00 = models.CharField(max_length=1, blank=True, null=True)
    blockce00 = models.CharField(max_length=4, blank=True, null=True)
    cousubfp00 = models.CharField(max_length=5, blank=True, null=True)
    submcdfp00 = models.CharField(max_length=5, blank=True, null=True)
    conctyfp00 = models.CharField(max_length=5, blank=True, null=True)
    placefp00 = models.CharField(max_length=5, blank=True, null=True)
    aiannhfp00 = models.CharField(max_length=5, blank=True, null=True)
    aiannhce00 = models.CharField(max_length=4, blank=True, null=True)
    comptyp00 = models.CharField(max_length=1, blank=True, null=True)
    trsubfp00 = models.CharField(max_length=5, blank=True, null=True)
    trsubce00 = models.CharField(max_length=3, blank=True, null=True)
    anrcfp00 = models.CharField(max_length=5, blank=True, null=True)
    elsdlea00 = models.CharField(max_length=5, blank=True, null=True)
    scsdlea00 = models.CharField(max_length=5, blank=True, null=True)
    unsdlea00 = models.CharField(max_length=5, blank=True, null=True)
    uace00 = models.CharField(max_length=5, blank=True, null=True)
    cd108fp = models.CharField(max_length=2, blank=True, null=True)
    sldust00 = models.CharField(max_length=3, blank=True, null=True)
    sldlst00 = models.CharField(max_length=3, blank=True, null=True)
    vtdst00 = models.CharField(max_length=6, blank=True, null=True)
    zcta5ce00 = models.CharField(max_length=5, blank=True, null=True)
    tazce00 = models.CharField(max_length=6, blank=True, null=True)
    ugace00 = models.CharField(max_length=5, blank=True, null=True)
    puma5ce00 = models.CharField(max_length=5, blank=True, null=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    blkgrpce = models.CharField(max_length=1, blank=True, null=True)
    blockce = models.CharField(max_length=4, blank=True, null=True)
    cousubfp = models.CharField(max_length=5, blank=True, null=True)
    submcdfp = models.CharField(max_length=5, blank=True, null=True)
    conctyfp = models.CharField(max_length=5, blank=True, null=True)
    placefp = models.CharField(max_length=5, blank=True, null=True)
    aiannhfp = models.CharField(max_length=5, blank=True, null=True)
    aiannhce = models.CharField(max_length=4, blank=True, null=True)
    comptyp = models.CharField(max_length=1, blank=True, null=True)
    trsubfp = models.CharField(max_length=5, blank=True, null=True)
    trsubce = models.CharField(max_length=3, blank=True, null=True)
    anrcfp = models.CharField(max_length=5, blank=True, null=True)
    ttractce = models.CharField(max_length=6, blank=True, null=True)
    tblkgpce = models.CharField(max_length=1, blank=True, null=True)
    elsdlea = models.CharField(max_length=5, blank=True, null=True)
    scsdlea = models.CharField(max_length=5, blank=True, null=True)
    unsdlea = models.CharField(max_length=5, blank=True, null=True)
    uace = models.CharField(max_length=5, blank=True, null=True)
    cd111fp = models.CharField(max_length=2, blank=True, null=True)
    sldust = models.CharField(max_length=3, blank=True, null=True)
    sldlst = models.CharField(max_length=3, blank=True, null=True)
    vtdst = models.CharField(max_length=6, blank=True, null=True)
    zcta5ce = models.CharField(max_length=5, blank=True, null=True)
    tazce = models.CharField(max_length=6, blank=True, null=True)
    ugace = models.CharField(max_length=5, blank=True, null=True)
    puma5ce = models.CharField(max_length=5, blank=True, null=True)
    csafp = models.CharField(max_length=3, blank=True, null=True)
    cbsafp = models.CharField(max_length=5, blank=True, null=True)
    metdivfp = models.CharField(max_length=5, blank=True, null=True)
    cnectafp = models.CharField(max_length=3, blank=True, null=True)
    nectafp = models.CharField(max_length=5, blank=True, null=True)
    nctadvfp = models.CharField(max_length=5, blank=True, null=True)
    lwflag = models.CharField(max_length=1, blank=True, null=True)
    offset = models.CharField(max_length=1, blank=True, null=True)
    atotal = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)
    tractce20 = models.CharField(max_length=6, blank=True, null=True)
    blkgrpce20 = models.CharField(max_length=1, blank=True, null=True)
    blockce20 = models.CharField(max_length=4, blank=True, null=True)
    countyfp20 = models.CharField(max_length=3, blank=True, null=True)
    statefp20 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faces'


class Featnames(models.Model):
    gid = models.AutoField(primary_key=True)
    tlid = models.BigIntegerField(blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    predirabrv = models.CharField(max_length=15, blank=True, null=True)
    pretypabrv = models.CharField(max_length=50, blank=True, null=True)
    prequalabr = models.CharField(max_length=15, blank=True, null=True)
    sufdirabrv = models.CharField(max_length=15, blank=True, null=True)
    suftypabrv = models.CharField(max_length=50, blank=True, null=True)
    sufqualabr = models.CharField(max_length=15, blank=True, null=True)
    predir = models.CharField(max_length=2, blank=True, null=True)
    pretyp = models.CharField(max_length=3, blank=True, null=True)
    prequal = models.CharField(max_length=2, blank=True, null=True)
    sufdir = models.CharField(max_length=2, blank=True, null=True)
    suftyp = models.CharField(max_length=3, blank=True, null=True)
    sufqual = models.CharField(max_length=2, blank=True, null=True)
    linearid = models.CharField(max_length=22, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    paflag = models.CharField(max_length=1, blank=True, null=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'featnames'


class Fieldmapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    tabela = models.CharField(max_length=60, blank=True, null=True)
    code = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fieldmapping'


class Fushat(models.Model):
    id = models.BigAutoField(primary_key=True)
    sourcefieldname = models.CharField(max_length=60, blank=True, null=True)
    destinationfieldname = models.CharField(max_length=60, blank=True, null=True)
    fieldtype = models.CharField(max_length=60, blank=True, null=True)
    domain = models.CharField(max_length=60, blank=True, null=True)
    domaincodefield = models.CharField(max_length=60, blank=True, null=True)
    domaindescription = models.CharField(max_length=60, blank=True, null=True)
    tabela1 = models.CharField(max_length=60, blank=True, null=True)
    fusha1 = models.CharField(max_length=60, blank=True, null=True)
    tabela2 = models.CharField(max_length=60, blank=True, null=True)
    fusha2 = models.CharField(max_length=60, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    tabela = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fushat'


class Gabime(models.Model):
    id = models.BigAutoField(primary_key=True)
    gabimi = models.CharField(max_length=3000, blank=True, null=True)
    tabela = models.CharField(max_length=60, blank=True, null=True)
    fusha = models.CharField(max_length=60, blank=True, null=True)
    vlera = models.CharField(max_length=60, blank=True, null=True)
    data = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gabime'


class GeocodeSettings(models.Model):
    name = models.TextField(primary_key=True)
    setting = models.TextField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    short_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geocode_settings'


class GeocodeSettingsDefault(models.Model):
    name = models.TextField(primary_key=True)
    setting = models.TextField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    short_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geocode_settings_default'


class Inclination(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'inclination'
        db_table_comment = 'Inclination class nomenclature (Flat, Slight slope, etc.)'


class Irrigationtype(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'irrigationtype'
        db_table_comment = 'Type of irrigation nomenclature (Free-running, dripping, etc.)'


class Kantina(models.Model):
    emri = models.CharField(unique=True, max_length=100, blank=True, null=True)
    qarku = models.ForeignKey('Qarqet', models.DO_NOTHING, db_column='qarku', to_field='id_qark', blank=True, null=True)
    bashkia = models.ForeignKey(Bashkite2014, models.DO_NOTHING, db_column='bashkia', to_field='id_bash', blank=True, null=True)
    fshati = models.ForeignKey('Villages', models.DO_NOTHING, db_column='fshati', to_field='code', blank=True, null=True)
    viti_krijimit = models.DateField(blank=True, null=True)
    patent = models.CharField(max_length=255, blank=True, null=True)
    certifikimi = models.CharField(max_length=100, blank=True, null=True)
    teknologjia_perdorur = models.CharField(max_length=255, blank=True, null=True)
    kapaciteti_ton = models.IntegerField(blank=True, null=True)
    prodhimi_ton = models.IntegerField(blank=True, null=True)
    shitja_brenda = models.IntegerField(blank=True, null=True)
    shitja_jashte = models.IntegerField(blank=True, null=True)
    dispo_vreshte_ha = models.IntegerField(blank=True, null=True)
    varieteti = models.ForeignKey('Variety', models.DO_NOTHING, db_column='varieteti', blank=True, null=True)
    prodhim_vete = models.IntegerField(blank=True, null=True)
    prodhim_te_trete = models.IntegerField(blank=True, null=True)
    importuar = models.IntegerField(blank=True, null=True)
    panaire_kombetare = models.BooleanField(blank=True, null=True)
    panaire_nderkombetare = models.BooleanField(blank=True, null=True)
    sasia_ton = models.IntegerField(blank=True, null=True)
    the_geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kantina'


class KantinaLloji(models.Model):
    kantina_id = models.IntegerField(primary_key=True)  # The composite primary key (kantina_id, klloji_code) found, that is not supported. The first column is selected.
    klloji_code = models.ForeignKey('Klloji', models.DO_NOTHING, db_column='klloji_code')

    class Meta:
        managed = False
        db_table = 'kantina_lloji'
        unique_together = (('kantina_id', 'klloji_code'),)


class KategoriLendaEPare(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'kategori_lenda_e_pare'
        db_table_comment = 'Domain per Kategoria e produkteve nga δshtδ prodhuar vera ( rrush, musht, verδ e re nδ fermentim)'


class KategoriaEProduktit(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'kategoria_e_produktit'
        db_table_comment = 'Domain per kategorite e produktit'


class Klloji(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'klloji'


class Layer(models.Model):
    topology = models.OneToOneField('Topology', models.DO_NOTHING, primary_key=True)  # The composite primary key (topology_id, layer_id) found, that is not supported. The first column is selected.
    layer_id = models.IntegerField()
    schema_name = models.CharField()
    table_name = models.CharField()
    feature_column = models.CharField()
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer'
        unique_together = (('topology', 'layer_id'), ('schema_name', 'table_name', 'feature_column'),)


class Listaeeneve(models.Model):
    id = models.BigAutoField(primary_key=True)
    ena_nr = models.IntegerField(blank=True, null=True, db_comment='ena numer')
    kapaciteti_ne_litra = models.FloatField(blank=True, null=True, db_comment='kapaciteti i enes ne litra')
    verejtje_shenime = models.CharField(max_length=255, blank=True, null=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', db_comment='id e deklaruesit te prodhimit')
    user_comments = models.CharField(max_length=255, blank=True, null=True)
    controller_comments = models.CharField(max_length=255, blank=True, null=True)
    statusi = models.ForeignKey('Status', models.DO_NOTHING, db_column='statusi', blank=True, null=True)
    vendndodhja = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listaeeneve'
        db_table_comment = ' tabele per listen e eneve'


class Listaematerialeve(models.Model):
    id = models.BigAutoField(primary_key=True)
    emri_substances = models.CharField(max_length=255, blank=True, null=True, db_comment='emri i substances')
    dataeveprimit = models.DateField(blank=True, null=True)
    furnizuesi = models.CharField(max_length=255, blank=True, null=True, db_comment=' Furnizuesi, Referenca e dokumentit')
    aplikuar_veres_nr = models.CharField(max_length=100, blank=True, null=True, db_comment='Aplikuar Verδs Numer')
    ena_nr = models.IntegerField(blank=True, null=True, db_comment='ena numer')
    sasia_furnizuar = models.FloatField(blank=True, null=True, db_comment='sasia e furnizuar ne kg')
    sasia_stok = models.FloatField(blank=True, null=True, db_comment='sasia stok ne kg')
    verejtje_shenime = models.CharField(max_length=255, blank=True, null=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', db_comment='id e deklaruesit te prodhimit')
    sasia_terhequr = models.FloatField(blank=True, null=True)
    vendndodhja = models.CharField(max_length=255, blank=True, null=True)
    user_comments = models.CharField(max_length=255, blank=True, null=True)
    controller_comments = models.CharField(max_length=255, blank=True, null=True)
    statusi = models.ForeignKey('Status', models.DO_NOTHING, db_column='statusi', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listaematerialeve'
        db_table_comment = ' tabele per listen e materialeve'


class LlojMushti(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'lloj_mushti'
        db_table_comment = 'Domain per llojin e mushtit'


class LoaderLookuptables(models.Model):
    process_order = models.IntegerField()
    lookup_name = models.TextField(primary_key=True, db_comment='This is the table name to inherit from and suffix of resulting output table -- how the table will be named --  edges here would mean -- ma_edges , pa_edges etc. except in the case of national tables. national level tables have no prefix')
    table_name = models.TextField(blank=True, null=True, db_comment='suffix of the tables to load e.g.  edges would load all tables like *edges.dbf(shp)  -- so tl_2010_42129_edges.dbf .  ')
    single_mode = models.BooleanField()
    load = models.BooleanField(db_comment="Whether or not to load the table.  For states and zcta5 (you may just want to download states10, zcta510 nationwide file manually) load your own into a single table that inherits from tiger.states, tiger.zcta5.  You'll get improved performance for some geocoding cases.")
    level_county = models.BooleanField()
    level_state = models.BooleanField()
    level_nation = models.BooleanField(db_comment='These are tables that contain all data for the whole US so there is just a single file')
    post_load_process = models.TextField(blank=True, null=True)
    single_geom_mode = models.BooleanField(blank=True, null=True)
    insert_mode = models.CharField(max_length=1)
    pre_load_process = models.TextField(blank=True, null=True)
    columns_exclude = models.TextField(blank=True, null=True, db_comment='List of columns to exclude as an array. This is excluded from both input table and output table and rest of columns remaining are assumed to be in same order in both tables. gid, geoid,cpi,suffix1ce are excluded if no columns are specified.')  # This field type is a guess.
    website_root_override = models.TextField(blank=True, null=True, db_comment='Path to use for wget instead of that specified in year table.  Needed currently for zcta where they release that only for 2000 and 2010')

    class Meta:
        managed = False
        db_table = 'loader_lookuptables'


class LoaderPlatform(models.Model):
    os = models.CharField(primary_key=True, max_length=50)
    declare_sect = models.TextField(blank=True, null=True)
    pgbin = models.TextField(blank=True, null=True)
    wget = models.TextField(blank=True, null=True)
    unzip_command = models.TextField(blank=True, null=True)
    psql = models.TextField(blank=True, null=True)
    path_sep = models.TextField(blank=True, null=True)
    loader = models.TextField(blank=True, null=True)
    environ_set_command = models.TextField(blank=True, null=True)
    county_process_command = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loader_platform'


class LoaderVariables(models.Model):
    tiger_year = models.CharField(primary_key=True, max_length=4)
    website_root = models.TextField(blank=True, null=True)
    staging_fold = models.TextField(blank=True, null=True)
    data_schema = models.TextField(blank=True, null=True)
    staging_schema = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loader_variables'


class MapsLocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    point = models.PointField()

    class Meta:
        managed = False
        db_table = 'maps_location'


class MbajtesiStokut(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mbajtesi_stokut'
        db_table_comment = 'Domain per mbajtesin e stokut'


class Mechanizationtype(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'mechanizationtype'
        db_table_comment = 'Type of mechanization nomenclature (Non mechanized, Mechanized, etc.)'


class Ngjyra(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ngjyra'
        db_table_comment = 'Domain per ngjyren e rrushit  i zi   , bardh, zi/kuq'


class Origjina(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'origjina'
        db_table_comment = 'Domain per origjinen e lendeve te para nga prodhohet vera'


class PagcGaz(models.Model):
    seq = models.IntegerField(blank=True, null=True)
    word = models.TextField(blank=True, null=True)
    stdword = models.TextField(blank=True, null=True)
    token = models.IntegerField(blank=True, null=True)
    is_custom = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pagc_gaz'


class PagcLex(models.Model):
    seq = models.IntegerField(blank=True, null=True)
    word = models.TextField(blank=True, null=True)
    stdword = models.TextField(blank=True, null=True)
    token = models.IntegerField(blank=True, null=True)
    is_custom = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pagc_lex'


class PagcRules(models.Model):
    rule = models.TextField(blank=True, null=True)
    is_custom = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagc_rules'


class PerdorimiIVreshtit(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'perdorimi_i_vreshtit'
        db_table_comment = 'domain per Forma e pδrdorimit tδ vreshtit: pronesi, bashkepronesi,perdorim me qera, perdorim pa pagese'


class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    secondname = models.CharField(max_length=30, blank=True, null=True)
    fathername = models.CharField(max_length=30, blank=True, null=True)
    birthdate = models.DateField()
    code = models.CharField(max_length=10, blank=True, null=True, db_comment='Code used only to identify surveyors')
    village = models.ForeignKey('Villages', models.DO_NOTHING, db_column='village', to_field='code', blank=True, null=True, db_comment='Village of residence.')
    legal = models.BooleanField(blank=True, null=True, db_comment='Is this a legal (as opposed to physical) person ?')

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'person'
        db_table_comment = 'A human being.'


class PersonFizikJuridik(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_fizik_juridik'


class Place(models.Model):
    gid = models.AutoField(unique=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    placefp = models.CharField(max_length=5, blank=True, null=True)
    placens = models.CharField(max_length=8, blank=True, null=True)
    plcidfp = models.CharField(primary_key=True, max_length=7)
    name = models.CharField(max_length=100, blank=True, null=True)
    namelsad = models.CharField(max_length=100, blank=True, null=True)
    lsad = models.CharField(max_length=2, blank=True, null=True)
    classfp = models.CharField(max_length=2, blank=True, null=True)
    cpi = models.CharField(max_length=1, blank=True, null=True)
    pcicbsa = models.CharField(max_length=1, blank=True, null=True)
    pcinecta = models.CharField(max_length=1, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.BigIntegerField(blank=True, null=True)
    awater = models.BigIntegerField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place'


class PlaceLookup(models.Model):
    st_code = models.IntegerField(primary_key=True)  # The composite primary key (st_code, pl_code) found, that is not supported. The first column is selected.
    state = models.CharField(max_length=2, blank=True, null=True)
    pl_code = models.IntegerField()
    name = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place_lookup'
        unique_together = (('st_code', 'pl_code'),)


class PointcloudFormats(models.Model):
    pcid = models.IntegerField(primary_key=True)
    srid = models.IntegerField(blank=True, null=True)
    schema = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pointcloud_formats'


class PozicioniPunes(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pozicioni_punes'


class Productiontype(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'productiontype'
        db_table_comment = 'Production destination nomenclature (Wine grape, Table grape, etc.)'


class Qarqet(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    id_qark = models.IntegerField(unique=True, blank=True, null=True)
    emer_qark = models.CharField(max_length=100, blank=True, null=True)
    qend_qark = models.CharField(max_length=100, blank=True, null=True)
    shape_length = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=32634, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qarqet'


class Referencegrid(models.Model):
    code = models.CharField(unique=True, max_length=4, db_comment="Combination of row position as letters (from 'A' to 'J') and column position as number.")
    the_geom = models.PolygonField(blank=True, null=True)
    colnum = models.IntegerField(blank=True, null=True)
    rownum = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referencegrid'
        db_table_comment = 'Reference grid for map sheets.'


class Regjistriprodhimit(models.Model):
    id = models.BigAutoField(primary_key=True)
    viti_vjeljes = models.IntegerField(blank=True, null=True, db_comment='viti i vjeljes se vreshtit')
    varieteti = models.ForeignKey('Variety', models.DO_NOTHING, db_column='varieteti', db_comment=' varieteti i vreshtit, me vlera nga tabela variety')
    vreshti_origjina = models.CharField(max_length=255, blank=True, null=True)
    vera_nr = models.IntegerField(blank=True, null=True, db_comment='vera numer')
    data_e_mbushjes = models.DateField(blank=True, null=True, db_comment='data e mbushjes se shisheve')
    numri_i_references = models.CharField(max_length=50, blank=True, null=True)
    permasat_e_shisheve = models.FloatField(blank=True, null=True, db_comment='permasat e shisheve ne litra')
    shishe_te_mbushura = models.BigIntegerField(blank=True, null=True, db_comment='Nr. i shisheve tδ mbushura')
    shishe_ne_dalje = models.IntegerField(blank=True, null=True, db_comment='Nr. i shisheve nδ dalje')
    stok = models.IntegerField(blank=True, null=True, db_comment='numri i shisheve stok')
    verejtje_shenime = models.CharField(max_length=255, blank=True, null=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', db_comment='id e deklaruesit te prodhimit')
    user_comments = models.CharField(max_length=255, blank=True, null=True)
    controller_comments = models.CharField(max_length=255, blank=True, null=True)
    statusi = models.ForeignKey('Status', models.DO_NOTHING, db_column='statusi', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regjistriprodhimit'
        db_table_comment = ' tabele per deklarimet e prodhimit'


class Rocktype(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'rocktype'
        db_table_comment = 'Type of rock nomenclature.'


class Role(models.Model):
    name = models.CharField(unique=True, max_length=80, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role'


class RolesUsers(models.Model):
    user_id = models.IntegerField(primary_key=True)  # The composite primary key (user_id, role_id) found, that is not supported. The first column is selected.
    role = models.ForeignKey(Role, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'roles_users'
        unique_together = (('user_id', 'role'),)


class Rootstock(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'rootstock'
        db_table_comment = 'Rootstock nomenclature'


class Rowsdirection(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'rowsdirection'
        db_table_comment = "General direction of plant rows' nomenclature."


class Rowsdirectiontype(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'rowsdirectiontype'
        db_table_comment = 'Rows direction nomenclature (Diagonal to the inclination, etc.)'


class RrushIVlefshemPer(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'rrush_i_vlefshem_per'
        db_table_comment = 'Domain per cilesine e rrushit te vlefshem per: me EOM, TGJM, TGJM varietore,vere(e thjeshte)'


class SecondaryUnitLookup(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    abbrev = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'secondary_unit_lookup'


class ShkuljeRimbjellje(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'shkulje_rimbjellje'
        db_table_comment = 'domain per shkulje ose rimbjellje'


class Soildepth(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'soildepth'
        db_table_comment = 'Soil depth class nomenclature(Too deep, Deep, Shallow, etc.)'


class Soiltype(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(unique=True, max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'soiltype'
        db_table_comment = 'Nomenclature of soil types.'


class State(models.Model):
    gid = models.AutoField(unique=True)
    region = models.CharField(max_length=2, blank=True, null=True)
    division = models.CharField(max_length=2, blank=True, null=True)
    statefp = models.CharField(primary_key=True, max_length=2)
    statens = models.CharField(max_length=8, blank=True, null=True)
    stusps = models.CharField(unique=True, max_length=2)
    name = models.CharField(max_length=100, blank=True, null=True)
    lsad = models.CharField(max_length=2, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.BigIntegerField(blank=True, null=True)
    awater = models.BigIntegerField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'


class StateLookup(models.Model):
    st_code = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=40, blank=True, null=True)
    abbrev = models.CharField(unique=True, max_length=3, blank=True, null=True)
    statefp = models.CharField(unique=True, max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state_lookup'


class Status(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'status'
        db_table_comment = 'statuset e te dhenave te deklaruara'


class StreetTypeLookup(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    abbrev = models.CharField(max_length=50, blank=True, null=True)
    is_hw = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'street_type_lookup'


class Supporttype(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'supporttype'
        db_table_comment = 'Type of support system nomenclature (No support, Individual support, etc.)'


class Surveystate(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'surveystate'
        db_table_comment = 'State of vineyard unit in the survey (Preliminary, Adjoined, etc.)'


class Tabblock(models.Model):
    gid = models.AutoField()
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    blockce = models.CharField(max_length=4, blank=True, null=True)
    tabblock_id = models.CharField(primary_key=True, max_length=16)
    name = models.CharField(max_length=20, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    ur = models.CharField(max_length=1, blank=True, null=True)
    uace = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tabblock'


class Tabblock20(models.Model):
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    blockce = models.CharField(max_length=4, blank=True, null=True)
    geoid = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=10, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    ur = models.CharField(max_length=1, blank=True, null=True)
    uace = models.CharField(max_length=5, blank=True, null=True)
    uatype = models.CharField(max_length=1, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)
    housing = models.FloatField(blank=True, null=True)
    pop = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tabblock20'


class TipKerkese(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tip_kerkese'


class Topology(models.Model):
    name = models.CharField(unique=True)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'topology'


class Tract(models.Model):
    gid = models.AutoField()
    statefp = models.CharField(max_length=2, blank=True, null=True)
    countyfp = models.CharField(max_length=3, blank=True, null=True)
    tractce = models.CharField(max_length=6, blank=True, null=True)
    tract_id = models.CharField(primary_key=True, max_length=11)
    name = models.CharField(max_length=7, blank=True, null=True)
    namelsad = models.CharField(max_length=20, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tract'


class UsGaz(models.Model):
    seq = models.IntegerField(blank=True, null=True)
    word = models.TextField(blank=True, null=True)
    stdword = models.TextField(blank=True, null=True)
    token = models.IntegerField(blank=True, null=True)
    is_custom = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'us_gaz'


class UsLex(models.Model):
    seq = models.IntegerField(blank=True, null=True)
    word = models.TextField(blank=True, null=True)
    stdword = models.TextField(blank=True, null=True)
    token = models.IntegerField(blank=True, null=True)
    is_custom = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'us_lex'


class UsRules(models.Model):
    rule = models.TextField(blank=True, null=True)
    is_custom = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'us_rules'


class User(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True, db_comment='emri i deklaruesit')
    last_name = models.CharField(max_length=50, blank=True, null=True, db_comment='mbiemri i deklaruesit')
    email = models.CharField(unique=True, max_length=255, blank=True, null=True, db_comment='emaili zyrtar i deklaruesit.')
    password = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    confirmed_at = models.DateTimeField(blank=True, null=True)
    last_login_at = models.DateTimeField(blank=True, null=True)
    current_login_at = models.DateTimeField(blank=True, null=True)
    last_login_ip = models.CharField(max_length=25, blank=True, null=True)
    current_login_ip = models.CharField(max_length=25, blank=True, null=True)
    login_count = models.IntegerField(blank=True, null=True)
    fs_uniquifier = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Userstatus(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'userstatus'
        db_table_comment = 'statusi i deklaruesit'


class Vaniardunittenant(models.Model):
    vineyardunit = models.OneToOneField('Vineyardunit', models.DO_NOTHING, db_column='vineyardunit', primary_key=True)  # The composite primary key (vineyardunit, owner) found, that is not supported. The first column is selected.
    owner = models.ForeignKey(Person, models.DO_NOTHING, db_column='owner')

    class Meta:
        managed = False
        db_table = 'vaniardunittenant'
        unique_together = (('vineyardunit', 'owner'),)


class VarietetColor(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'varietet_color'
        db_table_comment = 'ngjyra e varietetit te rrushit.'


class Variety(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80)
    registercode = models.CharField(max_length=20, blank=True, null=True, db_comment='Code used in the variety register, if any.')

    class Meta:
        managed = False
        db_table = 'variety'
        db_table_comment = 'Grape variety (Kalmet, etc.)'


class Varietypurity(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'varietypurity'
        db_table_comment = 'Class of variety purity nomenclature (Very purified, 1st category, etc.)'


class Villages(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    code = models.BigIntegerField(unique=True)
    emri_zk = models.CharField(max_length=60, blank=True, null=True)
    id_bash = models.CharField(max_length=50, blank=True, null=True)
    emer_bash = models.CharField(max_length=100, blank=True, null=True)
    qend_bash = models.CharField(max_length=100, blank=True, null=True)
    id_qark = models.CharField(max_length=50, blank=True, null=True)
    emer_qark = models.CharField(max_length=100, blank=True, null=True)
    qend_qark = models.CharField(max_length=100, blank=True, null=True)
    id_njqv = models.IntegerField(blank=True, null=True)
    emer_njqv = models.CharField(max_length=50, blank=True, null=True)
    emri_nga_tabela_village = models.CharField(max_length=50, blank=True, null=True)
    id_rrethi = models.IntegerField(blank=True, null=True)
    emer_rrethi = models.CharField(max_length=50, blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'villages'


class Vineyard(models.Model):
    mapcode = models.CharField(max_length=4, db_comment='Code of map sheet.')
    blockcode = models.CharField(max_length=3, db_comment='Code of block within map sheet.')
    unitcode = models.IntegerField(db_comment='Code of polygon within the block.')
    surveycode = models.CharField(max_length=30, blank=True, null=True, db_comment='Code used during survey.')

    class Meta:
        managed = False
        db_table = 'vineyard'
        db_table_comment = 'Vineyard: surface actually covered by vines without surrounding service areas.'


class Vineyardunit(models.Model):
    mapcode = models.CharField(max_length=4, db_comment='Code of map sheet as in the nation-wide grid.')
    blockcode = models.CharField(max_length=3, db_comment='Code of block within a map sheet.')
    farmcode = models.CharField(max_length=20, blank=True, null=True, db_comment="Code of unit's owner enterprise in the registry of farms.")
    fiscalcode = models.CharField(max_length=20, blank=True, null=True, db_comment="Tax code of the unit's owner.")
    prevsoiltype = models.ForeignKey(Soiltype, models.DO_NOTHING, db_column='prevsoiltype', blank=True, null=True, db_comment='Prevalent soil type on which the unit is located.')
    altitude = models.IntegerField(blank=True, null=True, db_comment='Altitude of parcle in meters')
    erosion = models.BooleanField(blank=True, null=True, db_comment='Presence of erosion.')
    soildepth = models.ForeignKey(Soildepth, models.DO_NOTHING, db_column='soildepth', blank=True, null=True, db_comment='Class of soil depth.')
    inclination = models.ForeignKey(Inclination, models.DO_NOTHING, db_column='inclination', blank=True, null=True, db_comment='Class of inclination.')
    exposure = models.ForeignKey(Exposure, models.DO_NOTHING, db_column='exposure', blank=True, null=True, db_comment='Facing of vineyard unit.')
    surface = models.FloatField(blank=True, null=True, db_comment='Surface of unit in square meters.')
    cultivationtype = models.ForeignKey(Cultivationtype, models.DO_NOTHING, db_column='cultivationtype', blank=True, null=True, db_comment='Cultivation type  and relation to other crop/orchard types.')
    rowsdistance = models.FloatField(blank=True, null=True, db_comment='Distance in centimeters between rows of plants.')
    plantsdistance = models.FloatField(blank=True, null=True, db_comment='Distance in centimeters between plsnts belonging to the same row.')
    couplesdistance = models.FloatField(blank=True, null=True, db_comment='Distance in centimeters between plants planted in couples.')
    supportsystem = models.ForeignKey(Supporttype, models.DO_NOTHING, db_column='supportsystem', blank=True, null=True, db_comment='Plant support system type.')
    cultivationform = models.ForeignKey(Cultivationform, models.DO_NOTHING, db_column='cultivationform', blank=True, null=True, db_comment='Form of cultivation and pruning.')
    mincultivationheight = models.FloatField(blank=True, null=True, db_comment='Minimum cultivation height in centimeters.')
    maxcultivationheight = models.FloatField(blank=True, null=True, db_comment='Maximum cultivation height in centimeters.')
    irrigationtype = models.ForeignKey(Irrigationtype, models.DO_NOTHING, db_column='irrigationtype', blank=True, null=True, db_comment='Type of irrigation (left empty if non-irrigated).')
    mechanizationtype = models.ForeignKey(Mechanizationtype, models.DO_NOTHING, db_column='mechanizationtype', blank=True, null=True, db_comment='Type of vineyard unit mechanization.')
    varietypurity = models.ForeignKey(Varietypurity, models.DO_NOTHING, db_column='varietypurity', blank=True, null=True, db_comment='Grade of purity of the grape variety.')
    principalvariety = models.ForeignKey(Variety, models.DO_NOTHING, db_column='principalvariety', blank=True, null=True, db_comment='Type of principal variety.')
    secondaryvariety = models.ForeignKey(Variety, models.DO_NOTHING, db_column='secondaryvariety', related_name='vineyardunit_secondaryvariety_set', blank=True, null=True, db_comment='Type of secondary grape variety.')
    othervariety = models.ForeignKey(Variety, models.DO_NOTHING, db_column='othervariety', related_name='vineyardunit_othervariety_set', blank=True, null=True, db_comment='Type of other grape variety.')
    notes = models.TextField(blank=True, null=True, db_comment='Type of other grape variety.')
    principalvarietyperc = models.IntegerField(blank=True, null=True, db_comment='Percentage of plant of the principal grape variety.')
    secondaryvarietyperc = models.IntegerField(blank=True, null=True, db_comment='Percentage of plant of the secondary grape variety.')
    othervarietyperc = models.IntegerField(blank=True, null=True, db_comment='Percentage of plants of the other grape variety.')
    the_geom = models.PolygonField(blank=True, null=True, db_comment='Geometry of the vineyard unit (a polygon)')
    rowsdirection = models.ForeignKey(Rowsdirection, models.DO_NOTHING, db_column='rowsdirection', blank=True, null=True, db_comment='General direction of rows')
    surveydate = models.DateField(blank=True, null=True, db_comment='Date of survey.')
    surveystate = models.ForeignKey(Surveystate, models.DO_NOTHING, db_column='surveystate', blank=True, null=True, db_comment='State of vineyard unit in survey.')
    unitcode = models.IntegerField(blank=True, null=True, db_comment='Unique code of vineyard unit within the block.')
    surveycode = models.CharField(max_length=30, blank=True, null=True, db_comment='Code used during the survey to identify the vineyard unit.')
    rootstocktype = models.ForeignKey(Rootstock, models.DO_NOTHING, db_column='rootstocktype', blank=True, null=True)
    surveyor = models.ForeignKey(Person, models.DO_NOTHING, db_column='surveyor', blank=True, null=True)
    implantationyear = models.IntegerField(blank=True, null=True, db_comment='Year of vineyard implantation')
    code = models.CharField(max_length=20, blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    fshati = models.ForeignKey(Villages, models.DO_NOTHING, db_column='fshati', to_field='code', blank=True, null=True, db_comment='code of village')
    bashkia = models.ForeignKey(Bashkite2014, models.DO_NOTHING, db_column='bashkia', to_field='id_bash', blank=True, null=True, db_comment='code of municipality')
    qarku = models.ForeignKey(Qarqet, models.DO_NOTHING, db_column='qarku', to_field='id_qark', blank=True, null=True, db_comment='code of region')
    area = models.IntegerField(blank=True, null=True, db_comment='area of polygon')

    class Meta:
        managed = False
        db_table = 'vineyardunit'
        unique_together = (('mapcode', 'blockcode', 'unitcode'),)
        db_table_comment = 'Table holding data about vineyard units'


class VineyardunitHist(models.Model):
    tid = models.BigIntegerField()
    mapcode = models.CharField(max_length=4)
    blockcode = models.CharField(max_length=3)
    farmcode = models.CharField(max_length=20, blank=True, null=True)
    fiscalcode = models.CharField(max_length=20, blank=True, null=True)
    prevsoiltype = models.BigIntegerField(blank=True, null=True)
    altitude = models.IntegerField(blank=True, null=True)
    erosion = models.BooleanField(blank=True, null=True)
    soildepth = models.BigIntegerField(blank=True, null=True)
    inclination = models.BigIntegerField(blank=True, null=True)
    exposure = models.BigIntegerField(blank=True, null=True)
    surface = models.FloatField(blank=True, null=True)
    cultivationtype = models.BigIntegerField(blank=True, null=True)
    rowsdistance = models.FloatField(blank=True, null=True)
    plantsdistance = models.FloatField(blank=True, null=True)
    couplesdistance = models.FloatField(blank=True, null=True)
    supportsystem = models.BigIntegerField(blank=True, null=True)
    cultivationform = models.BigIntegerField(blank=True, null=True)
    mincultivationheight = models.FloatField(blank=True, null=True)
    maxcultivationheight = models.FloatField(blank=True, null=True)
    irrigationtype = models.BigIntegerField(blank=True, null=True)
    mechanizationtype = models.BigIntegerField(blank=True, null=True)
    varietypurity = models.BigIntegerField(blank=True, null=True)
    principalvariety = models.BigIntegerField(blank=True, null=True)
    secondaryvariety = models.BigIntegerField(blank=True, null=True)
    othervariety = models.BigIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    principalvarietyperc = models.IntegerField(blank=True, null=True)
    secondaryvarietyperc = models.IntegerField(blank=True, null=True)
    othervarietyperc = models.IntegerField(blank=True, null=True)
    the_geom = models.PolygonField(blank=True, null=True)
    rowsdirection = models.BigIntegerField(blank=True, null=True)
    surveydate = models.DateField(blank=True, null=True)
    surveystate = models.BigIntegerField(blank=True, null=True)
    unitcode = models.IntegerField(blank=True, null=True)
    surveycode = models.CharField(max_length=30, blank=True, null=True)
    rootstocktype = models.BigIntegerField(blank=True, null=True)
    surveyor = models.BigIntegerField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    implantationyear = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    fshati = models.IntegerField(blank=True, null=True)
    bashkia = models.IntegerField(blank=True, null=True)
    qarku = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vineyardunit_hist'


class Vineyardunitowner(models.Model):
    vineyardunit = models.ForeignKey(Vineyardunit, models.DO_NOTHING, db_column='vineyardunit')
    owner = models.OneToOneField(Person, models.DO_NOTHING, db_column='owner', primary_key=True)  # The composite primary key (owner, vineyardunit) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'vineyardunitowner'
        unique_together = (('owner', 'vineyardunit'),)
        db_table_comment = 'Table implementing the many-to-many relationship between owners and vineyard units'


class Vineyardunitproduction(models.Model):
    vineyardunit = models.OneToOneField(Vineyardunit, models.DO_NOTHING, db_column='vineyardunit', primary_key=True)  # The composite primary key (vineyardunit, productiontype) found, that is not supported. The first column is selected.
    productiontype = models.ForeignKey(Productiontype, models.DO_NOTHING, db_column='productiontype')

    class Meta:
        managed = False
        db_table = 'vineyardunitproduction'
        unique_together = (('vineyardunit', 'productiontype'),)
        db_table_comment = 'Table implementing the many-to-many relationship between vineyard units and production types.'


class Vineyardunitrocktype(models.Model):
    vineyardunit = models.OneToOneField(Vineyardunit, models.DO_NOTHING, db_column='vineyardunit', primary_key=True)  # The composite primary key (vineyardunit, rocktype) found, that is not supported. The first column is selected.
    rocktype = models.ForeignKey(Rocktype, models.DO_NOTHING, db_column='rocktype')

    class Meta:
        managed = False
        db_table = 'vineyardunitrocktype'
        unique_together = (('vineyardunit', 'rocktype'),)
        db_table_comment = 'Table implementing the many-to-many relationship between vineyard units and rock types.'


class Vineyardunitsoiltype(models.Model):
    vineyardunit = models.OneToOneField(Vineyardunit, models.DO_NOTHING, db_column='vineyardunit', primary_key=True)  # The composite primary key (vineyardunit, soiltype) found, that is not supported. The first column is selected.
    soiltype = models.ForeignKey(Soiltype, models.DO_NOTHING, db_column='soiltype')
    type = models.IntegerField(blank=True, null=True, db_comment='Type of soil type for vineyarsd unit: 1 prmary: 2 secondary.')

    class Meta:
        managed = False
        db_table = 'vineyardunitsoiltype'
        unique_together = (('vineyardunit', 'soiltype'),)
        db_table_comment = 'Table implementing many to many relationship between vineyard units and soil types.'


class Vineyardunittenant(models.Model):
    vineyardunit = models.OneToOneField(Vineyardunit, models.DO_NOTHING, db_column='vineyardunit', primary_key=True)  # The composite primary key (vineyardunit, tenant) found, that is not supported. The first column is selected.
    tenant = models.ForeignKey(Person, models.DO_NOTHING, db_column='tenant')

    class Meta:
        managed = False
        db_table = 'vineyardunittenant'
        unique_together = (('vineyardunit', 'tenant'),)
        db_table_comment = 'Table implementing the many-to-many relationship between tenants and vineyard units'


class Vreshtatedeklaruar(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=35, blank=True, null=True)
    ortofoto = models.CharField(max_length=25, blank=True, null=True)
    blloku = models.CharField(max_length=25, blank=True, null=True)
    parcela = models.BigIntegerField(blank=True, null=True)
    kodi_fermes = models.CharField(max_length=25, blank=True, null=True)
    sip_totale_ha = models.FloatField(blank=True, null=True)
    sip_me_vreshta_ha = models.FloatField(blank=True, null=True)
    perqindj_me_vreshta = models.FloatField(blank=True, null=True)
    qarku = models.ForeignKey(Qarqet, models.DO_NOTHING, db_column='qarku', to_field='id_qark', blank=True, null=True)
    bashkia = models.ForeignKey(Bashkite2014, models.DO_NOTHING, db_column='bashkia', to_field='id_bash', blank=True, null=True)
    zona_kadastrale = models.ForeignKey(Villages, models.DO_NOTHING, db_column='zona_kadastrale', to_field='code', blank=True, null=True)
    perdorimi_i_vreshtit = models.ForeignKey(PerdorimiIVreshtit, models.DO_NOTHING, db_column='perdorimi_i_vreshtit', blank=True, null=True)
    varie1 = models.ForeignKey(Variety, models.DO_NOTHING, db_column='varie1', blank=True, null=True)
    varei1_color = models.ForeignKey(Ngjyra, models.DO_NOTHING, db_column='varei1_color', blank=True, null=True)
    varie1_sip = models.FloatField(blank=True, null=True)
    varie1_perq_sip = models.FloatField(blank=True, null=True)
    varie1_viti_mbjell = models.IntegerField(blank=True, null=True)
    varei1_vresht_me = models.ForeignKey(Eomtgjm, models.DO_NOTHING, db_column='varei1_vresht_me', blank=True, null=True)
    varie2 = models.ForeignKey(Variety, models.DO_NOTHING, db_column='varie2', related_name='vreshtatedeklaruar_varie2_set', blank=True, null=True)
    varei2_color = models.ForeignKey(Ngjyra, models.DO_NOTHING, db_column='varei2_color', related_name='vreshtatedeklaruar_varei2_color_set', blank=True, null=True)
    varie2_sip = models.FloatField(blank=True, null=True)
    varie2_perq_sip = models.FloatField(blank=True, null=True)
    varie2_viti_mbjell = models.IntegerField(blank=True, null=True)
    varei2_vresht_me = models.ForeignKey(Eomtgjm, models.DO_NOTHING, db_column='varei2_vresht_me', related_name='vreshtatedeklaruar_varei2_vresht_me_set', blank=True, null=True)
    varie3 = models.ForeignKey(Variety, models.DO_NOTHING, db_column='varie3', related_name='vreshtatedeklaruar_varie3_set', blank=True, null=True)
    varei3_color = models.ForeignKey(Ngjyra, models.DO_NOTHING, db_column='varei3_color', related_name='vreshtatedeklaruar_varei3_color_set', blank=True, null=True)
    varie3_sip = models.FloatField(blank=True, null=True)
    varie3_perq_sip = models.FloatField(blank=True, null=True)
    varie3_viti_mbjell = models.IntegerField(blank=True, null=True)
    varei3_vresht_me = models.ForeignKey(Eomtgjm, models.DO_NOTHING, db_column='varei3_vresht_me', related_name='vreshtatedeklaruar_varei3_vresht_me_set', blank=True, null=True)
    varie4 = models.ForeignKey(Variety, models.DO_NOTHING, db_column='varie4', related_name='vreshtatedeklaruar_varie4_set', blank=True, null=True)
    varei4_color = models.ForeignKey(Ngjyra, models.DO_NOTHING, db_column='varei4_color', related_name='vreshtatedeklaruar_varei4_color_set', blank=True, null=True)
    varie4_sip = models.FloatField(blank=True, null=True)
    varie4_perq_sip = models.FloatField(blank=True, null=True)
    varie4_viti_mbjell = models.IntegerField(blank=True, null=True)
    varei4_vresht_me = models.ForeignKey(Eomtgjm, models.DO_NOTHING, db_column='varei4_vresht_me', related_name='vreshtatedeklaruar_varei4_vresht_me_set', blank=True, null=True)
    varie5 = models.ForeignKey(Variety, models.DO_NOTHING, db_column='varie5', related_name='vreshtatedeklaruar_varie5_set', blank=True, null=True)
    varei5_color = models.ForeignKey(Ngjyra, models.DO_NOTHING, db_column='varei5_color', related_name='vreshtatedeklaruar_varei5_color_set', blank=True, null=True)
    varie5_sip = models.FloatField(blank=True, null=True)
    varie5_perq_sip = models.FloatField(blank=True, null=True)
    varie5_viti_mbjell = models.IntegerField(blank=True, null=True)
    varei5_vresht_me = models.ForeignKey(Eomtgjm, models.DO_NOTHING, db_column='varei5_vresht_me', related_name='vreshtatedeklaruar_varei5_vresht_me_set', blank=True, null=True)
    nr_hardhive = models.IntegerField(blank=True, null=True)
    dist_mes_bimeve = models.IntegerField(blank=True, null=True)
    dist_mes_rreshtave = models.IntegerField(blank=True, null=True)
    vresht_zone_me = models.ForeignKey('ZonemeEomtgjm', models.DO_NOTHING, db_column='vresht_zone_me', blank=True, null=True)
    emri_eom_tgjm = models.CharField(max_length=255, blank=True, null=True)
    perq_vere = models.FloatField(blank=True, null=True)
    perq_tavol = models.FloatField(blank=True, null=True)
    perq_ithare = models.FloatField(blank=True, null=True)
    perq_distil = models.FloatField(blank=True, null=True)
    perq_koleksion = models.FloatField(blank=True, null=True)
    perq_fidanishte = models.FloatField(blank=True, null=True)
    perq_vjoaktiv = models.FloatField(blank=True, null=True)
    perq_vshakterruar = models.FloatField(blank=True, null=True)
    shkulje_rimbjellje = models.ForeignKey(ShkuljeRimbjellje, models.DO_NOTHING, db_column='shkulje_rimbjellje', blank=True, null=True)
    data_shkuljerimbjellje = models.DateField(blank=True, null=True)
    data_deklarim = models.DateField(blank=True, null=True)
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userid', blank=True, null=True)
    the_geom = models.PolygonField(blank=True, null=True)
    user_comments = models.CharField(max_length=255, blank=True, null=True)
    controller_comments = models.CharField(max_length=255, blank=True, null=True)
    statusi = models.ForeignKey(Status, models.DO_NOTHING, db_column='statusi', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vreshtatedeklaruar'
        unique_together = (('ortofoto', 'blloku', 'parcela'),)


class Zcta5(models.Model):
    gid = models.AutoField(unique=True)
    statefp = models.CharField(max_length=2)
    zcta5ce = models.CharField(primary_key=True, max_length=5)  # The composite primary key (zcta5ce, statefp) found, that is not supported. The first column is selected.
    classfp = models.CharField(max_length=2, blank=True, null=True)
    mtfcc = models.CharField(max_length=5, blank=True, null=True)
    funcstat = models.CharField(max_length=1, blank=True, null=True)
    aland = models.FloatField(blank=True, null=True)
    awater = models.FloatField(blank=True, null=True)
    intptlat = models.CharField(max_length=11, blank=True, null=True)
    intptlon = models.CharField(max_length=12, blank=True, null=True)
    partflg = models.CharField(max_length=1, blank=True, null=True)
    the_geom = models.MultiPolygonField(srid=4269, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zcta5'
        unique_together = (('zcta5ce', 'statefp'),)


class ZipLookup(models.Model):
    zip = models.IntegerField(primary_key=True)
    st_code = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    co_code = models.IntegerField(blank=True, null=True)
    county = models.CharField(max_length=90, blank=True, null=True)
    cs_code = models.IntegerField(blank=True, null=True)
    cousub = models.CharField(max_length=90, blank=True, null=True)
    pl_code = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=90, blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_lookup'


class ZipLookupAll(models.Model):
    zip = models.IntegerField(blank=True, null=True)
    st_code = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    co_code = models.IntegerField(blank=True, null=True)
    county = models.CharField(max_length=90, blank=True, null=True)
    cs_code = models.IntegerField(blank=True, null=True)
    cousub = models.CharField(max_length=90, blank=True, null=True)
    pl_code = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=90, blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_lookup_all'


class ZipLookupBase(models.Model):
    zip = models.CharField(primary_key=True, max_length=5)
    state = models.CharField(max_length=40, blank=True, null=True)
    county = models.CharField(max_length=90, blank=True, null=True)
    city = models.CharField(max_length=90, blank=True, null=True)
    statefp = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_lookup_base'


class ZipState(models.Model):
    zip = models.CharField(primary_key=True, max_length=5)  # The composite primary key (zip, stusps) found, that is not supported. The first column is selected.
    stusps = models.CharField(max_length=2)
    statefp = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_state'
        unique_together = (('zip', 'stusps'),)


class ZipStateLoc(models.Model):
    zip = models.CharField(primary_key=True, max_length=5)  # The composite primary key (zip, stusps, place) found, that is not supported. The first column is selected.
    stusps = models.CharField(max_length=2)
    statefp = models.CharField(max_length=2, blank=True, null=True)
    place = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'zip_state_loc'
        unique_together = (('zip', 'stusps', 'place'),)


class ZonemeEomtgjm(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'zoneme_eomtgjm'
        db_table_comment = 'zone me EOM, TGJM '