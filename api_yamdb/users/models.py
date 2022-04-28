from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

ROLE_CHOICES = (
    ('user', 'пользователь'),
    ('moderator', 'модератор'),
    ('admin', 'администратор'),
)


class MyValidator(UnicodeUsernameValidator):
    regex = r'^[\w.@+-]+\z'


class User(AbstractUser):
    username_validator = MyValidator()
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
    )
    email = models.EmailField('E-mail', unique=True,)
    bio = models.TextField('Биография', null=True, blank=True,)
    role = models.CharField(
        'Тип пользователя',
        choices=ROLE_CHOICES,
        default='user',
    )

    REQUIRED_FIELDS = ['username', 'email']
