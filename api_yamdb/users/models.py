import secrets
import string

from django.contrib.auth.models import AbstractUser
from django.db import models


def generate_confirmation_code() -> str:
    """ Генерация случайного кода. """
    letters_and_digits = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(letters_and_digits) for i in range(6))


ROLE_CHOICES = (
    ('user', 'пользователь'),
    ('moderator', 'модератор'),
    ('admin', 'администратор'),
)


class User(AbstractUser):
    """ Модель пользователя. """
    email = models.EmailField('E-mail', max_length=254, unique=True,)
    bio = models.TextField('Биография', null=True, blank=True,)
    role = models.CharField(
        'Тип пользователя',
        max_length=30,
        choices=ROLE_CHOICES,
        default='user',
    )
    confirmation_code = models.CharField(
        max_length=6,
        default=generate_confirmation_code
    )
