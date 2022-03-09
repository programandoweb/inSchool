from django.db import models
#import datetime

class GroupTypeUserApp(models.Model):
    ma_grouptype_user_id =   models.AutoField(primary_key=True)
    label                =   models.CharField(max_length=255, blank=True, null=True)
    token                =   models.CharField(max_length=255,blank=True, null=True)    
    
    class Meta:
        ordering    =   ['label']

    fields          =   ('label')
    list_display    =   ('label')
    
    def __str__(self):
        return self.label

class TypeUserApp(models.Model):
    ma_grouptype_user_id    =   models.ForeignKey(GroupTypeUserApp,on_delete=models.CASCADE)
    ma_type_user_id         =   models.AutoField(primary_key=True)    
    label                   =   models.CharField(max_length=255, blank=True)
    token                   =   models.CharField(max_length=255,blank=True, null=True,verbose_name="Nombre")    
    
    class Meta:
        ordering    =   ['label']

    fields          =   ('label')
    list_display    =   ('label')
    
    def __str__(self):
        return self.label
    
        

class UserApp(models.Model):
    ma_type_user_id =   models.ForeignKey(TypeUserApp,on_delete=models.CASCADE)
    user_id         =   models.AutoField(primary_key=True)    
    names           =   models.CharField(max_length=30)
    lastnames       =   models.CharField(max_length=30)
    document        =   models.CharField(max_length=12,unique=True)
    email           =   models.EmailField(max_length=255,unique=True)
    password        =   models.CharField(max_length=250)  
    token           =   models.CharField(max_length=560,blank=True)  
    token_operation =   models.CharField(max_length=560,blank=True)  
    avatar          =   models.CharField(max_length=500,blank=True)
    is_active       =   models.BooleanField(default=0)
    objects         =   models.Manager() 

    USERNAME_FIELD  =   'email'
    REQUIRED_FIELD  =   ['names', 'lastnames']
    fields          =   ('names', 'lastnames')
    list_display    =   ('names', 'lastnames', 'email')

    def __str__(self):
        return f"{self.names}  {self.lastnames}  ({self.document})"

 
