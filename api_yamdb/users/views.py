import secrets
import string

from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CreateUserSerializer, TokenObtainSerializer
from .models import User


def generate_confirmation_code() -> str:
    """ Генерация случайного кода. """
    letters_and_digits = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(letters_and_digits) for i in range(6))


@api_view(['POST'])
def register_user(request):
    """ Регистрация нового пользователя. """
    serializer = CreateUserSerializer(data=request.data)
    try:
        user = User.objects.get(username=request.data['username'])
    except Exception:
        user = None
    if (
        serializer.is_valid()
        or (
            user and user.email == serializer.initial_data['email']
            and not user.confirmation_code
        )
    ):
        if not user:
            user = serializer.save()
        user.confirmation_code = generate_confirmation_code()
        user.save()
        send_mail(
            'Registration on YaMDb',
            f'Your verification code to receive a token: '
            f'{user.confirmation_code}',
            'YaMDb@example.com',
            [user.email],
            fail_silently=False,
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


class TokenObtainView(TokenObtainPairView):
    """ Получение токена. """
    serializer_class = TokenObtainSerializer
