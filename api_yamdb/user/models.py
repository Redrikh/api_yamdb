from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    role = models.TextField(
        'Права пользователя',
        blank=False,
        default='user',
    )
    bio = models.TextField(
        'Информация о пользователе',
        blank=True,
    )
