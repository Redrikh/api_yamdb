from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя."""

    class Meta:
        fields = (
            'username', 'bio', 'email', 'first_name', 'last_name', 'role',
        )
        model = User
