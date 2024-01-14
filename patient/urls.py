from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivateAccount, PatientViewSets, UserLoginAPIView, UserRegistrationAPIView, UserLogoutView


router = DefaultRouter()
router.register('list', PatientViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    # path('active/<uid64>/<token>/', views.activate, name = 'activate'),# function based activation
    path('active/<str:uid64>/<str:token>', ActivateAccount.as_view(), name='activate_account'), # class based activation
   path('logout/', UserLogoutView.as_view(), name='logout'),
]
