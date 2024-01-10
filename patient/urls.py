from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSets


router = DefaultRouter()
router.register('list', PatientViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
