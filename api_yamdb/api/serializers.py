from rest_framework import serializers
from djoser.serializers import UserSerializer

from reviews.models import (
    Category,
    Genre,
    Title,
    Review,
    Comment,
)
from user.models import User


class CategorieSerializer(serializers.ModelSerializer):
    """Сериализатор для категорий."""

    class Meta:
        fields = '__all__'
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для жанров."""

    class Meta:
        fields = '__all__'
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    """Сериализатор для заголовка."""

    class Meta:
        fields = '__all__'
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для ревью."""

    class Meta:
        fields = '__all__'
        model = Review


class AuthSerializer(serializers.ModelSerializer):
    """Сериализатор для Auth."""

    class Meta:
        fields = '__all__'
        model = User


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя."""

    class Meta:
        fields = '__all__'
        model = User
