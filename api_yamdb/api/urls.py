from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import (
    CategoryViewSet,
    GenreViewSet,
    TitleViewSet,
    ReviewViewSet,
    UsersViewSet,
    CommentViewSet,
)

router = DefaultRouter()

router.register(r'users', UsersViewSet, basename='user')
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet, basename='titles')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='titles',
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='titles',
)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.authtoken')),
    path('v1/auth/', include('djoser.urls.jwt')),
    path('v1/categories/<slug>', CategoryViewSet.as_view({'get': 'retrieve'})),
    path('v1/genres/<slug>', GenreViewSet.as_view({'get': 'retrieve'})),
]
