from django.contrib.auth import get_user_model
from rest_framework import serializers

from reviews.models import (
    Category,
    Genre,
    Title,
    Review,
    Comment,
)
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя."""

    class Meta:
        fields = (
            'username',
            'bio',
            'email',
            'first_name',
            'last_name',
            'role'
        )
        model = User

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Создать пользователя me нельзя'
            )
        return value


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий."""

    class Meta:
        fields = ('name', 'slug',)
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для жанров."""

    class Meta:
        fields = ('name', 'slug',)
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    """Сериализатор для заголовка."""
    rating = serializers.IntegerField(
        source='reviews__score__avg',
        read_only=True,
    )

    class Meta:
        fields = ('id', 'name', 'year', 'rating',)
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для ревью."""
    title = serializers.SlugRelatedField(
        read_only=True, slug_field='name'
    )
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Review

    def validate(self, data):
        request = self.context.get('request')
        queryset = self.context.get('view').get_queryset()
        if request.method == 'PATCH':
            return data
        if queryset.filter(author=request.user).exists():
            raise serializers.ValidationError(
                'Нельзя оставлять больше 1 отзыва на произведение'
            )
        return data


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment
