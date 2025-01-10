from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('news', NewsViewSet)
router.register('admins', AdministrationViewSet)
router.register('jobs', JobsViewSet)
router.register('earths', EarthViewSet)
router.register('agriculturals', AgriculturalViewSet)
router.register('statelands', StateLandViewSet)
router.register('resolutions', ResolutionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]