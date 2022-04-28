from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import (
    Category,
    Genre,
    Title,
    Review,
    User,
)
from .permissions import (
    IsAdminOrReadOnly,
    IsModeratorOrReadOnly,
    IsOwnerOrReadOnly,
)
from .serializers import (
    CategorieSerializer,
    GenreSerializer,
    TitleSerializer,
    ReviewSerializer,
    CommentSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """Вьюсет для пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAdminUser,
    ]
    pagination_class = LimitOffsetPagination
    search_fields = ('user__username')


class CategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет для категорий."""

    queryset = Category.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    pagination_class = LimitOffsetPagination


class GenreViewSet(viewsets.ModelViewSet):
    """Вьюсет для жанров."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [
        IsAdminOrReadOnly,
    ]


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет для заголовков."""

    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [
        IsAdminOrReadOnly,
    ]


class ReviewViewSet(viewsets.ModelViewSet):
    """Вьюсет для ревью."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [
        IsAdminOrReadOnly,
        IsModeratorOrReadOnly,
        IsOwnerOrReadOnly,
    ]


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для комментариев."""

    serializer_class = CommentSerializer
    permission_classes = [
        IsAdminOrReadOnly,
        IsModeratorOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id')
        )
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id')
        )
        serializer.save(author=self.request.user, review=review)
