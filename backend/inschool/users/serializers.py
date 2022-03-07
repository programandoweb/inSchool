from rest_framework import serializers
from users.models import UserApp,TypeUserApp

class TypeUserAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeUserApp
        fields = ['label','token']

class UserSerializerNew(serializers.HyperlinkedModelSerializer):
    group           =   TypeUserAppSerializer(many=True,read_only=True)
    class Meta:        
        model       =   UserApp
        fields      =   ('names','lastnames','email','group')

class UserSerializer(serializers.Serializer):
    """Serialized for users information"""
    names           =   serializers.CharField(max_length=30)
    lastnames       =   serializers.CharField(max_length=30)
    email           =   serializers.EmailField(max_length=255)
    document        =   serializers.CharField(max_length=12)
    password        =   serializers.CharField(max_length=250)  
    

class FirtsSerializer(serializers.Serializer):
    """Serializer for testing"""
    name    =   serializers.CharField(max_length=10)

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model   =   UserApp  
        exclude =   ['password']  
          