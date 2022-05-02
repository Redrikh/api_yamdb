from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework import viewsets
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

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

    def get_username(self):
        username = self.kwargs.get('username')
        if username == 'me':
            username = self.request.user.username
        user = get_object_or_404(User, username=username)
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
    filter_fields = ('category__slug')
    lookup_field = 'slug'

    def get_slug(self):
        category_name = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=category_name)
        serializer = CategorieSerializer(category)
        return Response(serializer.data)


class GenreViewSet(viewsets.ModelViewSet):
    """Вьюсет для жанров."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    pagination_class = PageNumberPagination
    search_fields = ('genre__slug')
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
