from email import message
from rest_framework.views import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth.hashers import make_password #,check_password

from .serializers import UserSerializer,UserSerializerNew,TypeUserAppSerializer,ListStudientsSerializer,ListAttendeesSerializer,GroupUserAppSerializer,UserLoginSerializer, UserModelSerializer
from users import serializers
from .models import UserApp,TypeUserApp,GroupTypeUserApp




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

    queryset            = UserApp.objects.all()
    serializer_class    = UserSerializerNew  

    @action(detail=False)
    def studients(self, request):
        retornar            = UserApp.objects.filter(ma_type_user_id=9)
        serializer          = UserSerializerNew(retornar, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def attendees(self, request):
        retornar            = UserApp.objects.filter(ma_type_user_id=8)
        serializer          = UserSerializerNew(retornar, many=True)
        return Response(serializer.data)    


class PaginationTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint match Types users.
    """
    queryset            = TypeUserApp.objects.all()
    serializer_class    = TypeUserAppSerializer

class PaginationGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint match Types users.
    """
    queryset            = GroupTypeUserApp.objects.all()
    serializer_class    = GroupUserAppSerializer

class LoginViewSet(viewsets.ModelViewSet):
    
    queryset = UserApp.objects.all()
    serializer_class = UserLoginSerializer

    # Detail define si es una petición de detalle o no, 
    # en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @action(detail=False, methods=['post','get'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)    