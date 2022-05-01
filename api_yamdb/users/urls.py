from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views
from .views import TokenObtainView

app_name = 'users'

urlpatterns = [
    path('signup/', views.register_user, name='registration'),
    path('token/', TokenObtainView.as_view(), name='token_obtain_pair'),
]
