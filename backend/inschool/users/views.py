from email import message
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password #,check_password

from .serializers import UsersSerializers,UserSerializerNew,TypeUserAppSerializer
from users import serializers
from .models import UserApp,TypeUserApp






def intro():
    return {  'Developing': {   'Developed by':'ProgramandoWeb.net',
                                'Developer':'Jorge Méndez',
                                'Phone':'3115000926',
                                'Email':'info@programandoweb.net',
                                'Country':'Colombia'}
               }

def encode_password(variable):
    return make_password(variable)

class PaginationUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset            = UserApp.objects.all().select_related('ma_type_user_id').order_by('names')
    serializer_class    = UserSerializerNew  

    def set_comment(self, request, pk=None):
        my_post = self.get_object()  
        serializer = TypeUserAppSerializer(data=request.data)                 
        if serializer.is_valid():
            serializer.save(post=my_post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaginationGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset            = TypeUserApp.objects.all().select_related('ma_grouptype_user_id').order_by('label')
    serializer_class    = TypeUserAppSerializer  


class UsersView(APIView):    
    ma_type_user_id     =   1
    serializer_class    =   serializers.UserSerializer
    
    def get(self,request,format=None):
        #users       =   UserApp.objects.all().select_related('parametro')
        users        =   UserApp.objects.select_related('ma_type_user_id')
        
        #return print(users)

        serializer   =   UsersSerializers(users, many=True)
        
        

        if serializer:
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    
class UserView(APIView):

    
    serializer_class    =   serializers.UserSerializer

    def get(self,request,format=None):
        
        return Response(intro())

    def post(self,request):
        """ 
            MI PRIMER POST, AL HACER ESO, ME MOSTRARÁ UN INPUT DEBAJO PARA CARGAR INFORMACIÓN
            ES IMPORTANTE RESALTAR QUE CUANDO CREAMOS NUESTRO SERIALIZER DEFINIMOS LA VARIABLE NAME
            CON MÁSXIMO 10 CARACTERES, LO QUE NOS GENERARÁ UN ERORR SI EL INPUT ENVÍA MÁS CARACTERES
            DE LOS PERMITIDOS
        """
        serializer  =   self.serializer_class(data=request.data)

        if serializer.is_valid():

            password_post   =   encode_password(serializer.validated_data.get('password'))
            
            UserApp.objects.create(
                            names       =   serializer.validated_data.get('names'),
                            lastnames   =   serializer.validated_data.get('lastnames'),
                            email       =   serializer.validated_data.get('email'),
                            document    =   serializer.validated_data.get('document'),
                            token_operation   =   "init",
                            password    =   password_post,
                            token       =   f'user_{password_post}'
                        )

            names       =   serializer.validated_data.get('names')
            message     =   f'Hello {names} data success'

            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):       
        """Actualizar un obejto"""
        return Response({'METHOD':'put'})

    def patch(self,request,pk=None):       
        """Actualizar PARCIAL UN OBJETO sólo un campo de la tabla"""
        return Response({'METHOD':'PATH'})

    def delete(self,request,pk=None):       
        """Actualizar PARCIAL UN OBJETO sólo un campo de la tabla"""
        return Response({'METHOD':'DELETE'})        