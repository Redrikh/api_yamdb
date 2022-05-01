from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CreateUserSerializer, TokenObtainSerializer
from .models import User


@api_view(['POST'])
def register_user(request):
    """ Регистрация нового пользователя. """

    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        current_user = User.objects.last()
        send_mail(
            'Registration on YaMDb',
            f'Your verification code to receive a token: '
            f'{current_user.confirmation_code}',
            'YaMDb@example.com',
            [current_user.email],
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
