from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('news', NewsViewSet)
router.register('administrations', AdministrationViewSet)
router.register('jobs', JobsViewSet)
router.register('earths', EarthViewSet)
router.register('agriculturals', AgriculturalViewSet)
router.register('statelands', StateLandViewSet)
router.register('resolutions', ResolutionViewSet)
router.register('glava', GlavaViewSet)
router.register('admins', AdminsViewSet)


urlpatterns = [
    path('contact/', contact_form, name='contact_form'),
    path('', include(router.urls)),
]