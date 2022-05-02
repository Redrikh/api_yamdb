from rest_framework import viewsets

from .serializers import UserSerializer
from users.models import User
from .permissions import IsAdmin


class UsersViewSet(viewsets.ModelViewSet):
    """Вьюсет для пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAdmin,
    ]
    search_fields = ('user__username')
    lookup_field = 'username'
