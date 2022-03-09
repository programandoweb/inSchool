from rest_framework import serializers
from users.models import UserApp,TypeUserApp,GroupTypeUserApp
from rest_framework.authtoken.models import Token
from django.contrib.auth import password_validation, authenticate


class UserModelSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = UserApp
        fields = (
            'email',
            'password',
        )

class UserLoginSerializer(serializers.Serializer):
    
    # Campos que vamos a requerir
    email       = serializers.EmailField()
    password    = serializers.CharField(min_length=8, max_length=64)

    # Primero validamos los datos
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError(f'Las credenciales no son válidas { data["email"] }')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class GroupUserAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupTypeUserApp
        fields = ['label','token']

class TypeUserAppSerializer(serializers.HyperlinkedModelSerializer):
    """This relationship only get return self.label fron model, example 'Súperusuario' """
    ma_grouptype_user_id  =   serializers.StringRelatedField(read_only=True)
    class Meta:
        model = TypeUserApp
        fields = ['ma_grouptype_user_id','label','token']

class UserSerializerNew(serializers.HyperlinkedModelSerializer):
    
    """
        This relation ship is for One to One
        this need call the field with foreign key declarated in the model, example  ma_type_user_id     
    """
    #ma_type_user_id  =   TypeUserAppSerializer(read_only=True)
    

    """This relationship only get return self.label fron model, example 'Súperusuario' """
    ma_type_user_id  =   serializers.StringRelatedField(read_only=True)
        
    class Meta:        
        model       =   UserApp
        fields      =   ('ma_type_user_id','names','lastnames','email')    

class ListStudientsSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:        
        model       =   UserApp
        fields      =   ('names','lastnames','email')

class ListAttendeesSerializer(serializers.HyperlinkedModelSerializer):
    
    """
        This relation ship is for One to One
        this need call the field with foreign key declarated in the model, example  ma_type_user_id     
    """
    
    #ma_type_user_id  =   TypeUserAppSerializer(read_only=True)
    

    """This relationship only get return self.label fron model, example 'Súperusuario' """
    #ma_type_user_id  =   serializers.StringRelatedField(read_only=True)
        
    class Meta:        
        model       =   UserApp
        fields      =   ('names','lastnames','email')            
        

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
        fields  =   ('email','password')
        #exclude =   ['password']  
          