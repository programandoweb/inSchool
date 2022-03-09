from django.urls import include, path
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r'list', views.PaginationUserViewSet)
router.register(r'groups', views.PaginationGroupViewSet)
router.register(r'types', views.PaginationTypeViewSet)
router.register(r'auth', views.LoginViewSet)
#router.register(r'login', views.LoginViewSet)

#urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls))
]