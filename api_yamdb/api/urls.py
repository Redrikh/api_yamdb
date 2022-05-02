from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import UsersViewSet

router = DefaultRouter()

router.register(r'users', UsersViewSet, basename='user-detail')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('users.urls')),
]
