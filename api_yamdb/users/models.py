from django.contrib.auth.models import AbstractUser
from django.db import models

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
        blank=True
    )

    class Meta:
        ordering = ['username']
