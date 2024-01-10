
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our ViewSets with it. joto view hobe sob register korte hobe 
# router die url pattern use kora hoyeche karon ek sathe update, delete, view, put sob kora jabe er jonno kono notun view likha lagbe , tai router use kora hoise arki 
router = DefaultRouter()
router.register('', views.ServiceViewSet)

# The API URLs are now determined automatically by the router. sob home a thakbe tai '' empty use kora hoise
urlpatterns = [
    path('', include(router.urls)),
]