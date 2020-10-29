from rest_framework import routers
from .api import RegViewSet
from .api import RegViewSet2


router = routers.DefaultRouter()
router.register('api/myreg',RegViewSet,'myreg')
router.register('api/login',RegViewSet2,'myreg')
urlpatterns = router.urls 