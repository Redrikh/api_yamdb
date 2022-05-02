from django.shortcuts import get_object_or_404
from requests import Response, request
from rest_framework import viewsets, status, filters
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)
from rest_framework.exceptions import NotFound
from rest_framework.decorators import action

from reviews.models import (
    Category,
    Genre,
    Title,
    Review,
)
from users.models import User
from .permissions import (
    IsAdmin,
    IsAdminOrReadOnly,
    IsModeratorOrReadOnly,
)
from .serializers import (
    CategorieSerializer,
    GenreSerializer,
    TitleSerializer,
    ReviewSerializer,
    CommentSerializer,
    UserSerializer,
)


class UsersViewSet(viewsets.ModelViewSet):
    """Вьюсет для пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAdmin,
    ]
    pagination_class = PageNumberPagination
    search_fields = ('user__username')
    lookup_field = 'username'

    @action(detail=True, url_path='me')
    def me(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет для категорий."""

    queryset = Category.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(viewsets.ModelViewSet):
    """Вьюсет для жанров."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'

    def get_slug(self):
        genre_name = self.kwargs.get('slug')
        genre = get_object_or_404(Genre, slug=genre_name)
        serializer = CategorieSerializer(genre)
        return Response(serializer.data)


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет для заголовков."""

    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    pagination_class = PageNumberPagination


class ReviewViewSet(viewsets.ModelViewSet):
    """Вьюсет для ревью."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
        IsAdminOrReadOnly,
        IsModeratorOrReadOnly,
    ]


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для комментариев."""

    serializer_class = CommentSerializer
    permission_classes = [
        IsAdminOrReadOnly,
        IsModeratorOrReadOnly,
    ]
