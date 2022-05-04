from rest_framework.routers import DefaultRouter
from django.urls import include, path
from users.views import TokenObtainView, register_user

from .views import (
    CategoryViewSet,
    GenreViewSet,
    TitleViewSet,
    ReviewViewSet,
    UsersViewSet,
    CommentViewSet,
)

router = DefaultRouter()

router.register(r'users', UsersViewSet)
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
    path('v1/auth/signup/', register_user, name='registration'),
    path(
        'v1/auth/token/',
        TokenObtainView.as_view(),
        name='token_obtain_pair'
    ),
]
