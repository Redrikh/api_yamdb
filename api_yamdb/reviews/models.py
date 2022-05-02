from django.db import models

from users.models import User


CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
)


class Genre(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True,
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True,
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=200,
    )
    year = models.IntegerField()
    categories = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
    )
    genres = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        through_fields=('title', 'genre'),
        related_name='titles',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'categories'],
                name='unique_name_categories'
            )
        ]

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.title} {self.genre}'


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    score = models.CharField(
        max_length=2,
        choices=CHOICES,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_title_author'
            )
        ]

    def __str__(self):
        return self.text[:25]


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.text[:25]