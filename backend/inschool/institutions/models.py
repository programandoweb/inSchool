from xml.etree.ElementInclude import default_loader
from django.db import models
from django.utils.timezone import now


class InstitutionApp(models.Model):
    institution_id  =   models.AutoField(primary_key=True)    
    name            =   models.CharField(max_length=100)    
    social_reasons  =   models.CharField(max_length=100)    
    nit             =   models.CharField(max_length=12,unique=True)
    website         =   models.CharField(max_length=255,unique=True)
    email           =   models.EmailField(max_length=255,unique=True)
    legal_representative_name       =   models.CharField(max_length=100)    
    legal_representative_document   =   models.CharField(max_length=100)    
    token           =   models.CharField(max_length=560,blank=True)  
    avatar          =   models.CharField(max_length=500,blank=True)
    register_date   =   models.DateTimeField(default=now)
    is_active       =   models.BooleanField(default=0)

    REQUIRED_FIELD  =   ['name', 'nit']
    fields          =   ('name', 'nit')
    list_display    =   ('name', 'nit', 'email')

    def __str__(self):
        return self.name


class HeadquartersInstitutionApp(models.Model):
    institution_id  =   models.ForeignKey(InstitutionApp,on_delete=models.CASCADE)
    Headquarters_id =   models.AutoField(primary_key=True)
    name            =   models.CharField(max_length=100)
    direction       =   models.CharField(max_length=500)
    phone           =   models.CharField(max_length=30)
    email           =   models.EmailField(max_length=255,unique=True)
    register_date   =   models.DateTimeField(default=now)

    REQUIRED_FIELD  =   ['name']
    fields          =   ('name')
    list_display    =   ('name','email')

    def __str__(self):
        return self.name
