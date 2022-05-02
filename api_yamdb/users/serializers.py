from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class CreateUserSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания пользователя. """

    class Meta:
        fields = ('email', 'username',)
        model = User

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Using name "me" is prohibited!'
            )
        return value


class TokenObtainSerializer(TokenObtainPairSerializer):
    """ Сериализатор для получения токена. """

    username_field = User.USERNAME_FIELD

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.fields['confirmation_code'] = serializers.CharField()

    def validate(self, attrs):
        current_user = get_object_or_404(
            User, username=attrs[self.username_field]
        )
        if current_user.confirmation_code != attrs['confirmation_code']:
            raise serializers.ValidationError(
                'Wrong confirmation code!'
            )
        refresh = RefreshToken.for_user(current_user)
        # self.get_token(current_user)
        return {'token': str(refresh.access_token)}
