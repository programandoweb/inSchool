from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r'list', views.PaginationUserViewSet)
router.register(r'groups', views.PaginationGroupViewSet)

urlpatterns = router.urls
