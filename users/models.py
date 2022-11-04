from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class UserRoles:
    USER = 'member'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    choices = (
        ("Пользователь", USER),
        ("Админ", ADMIN),
        ("Модератор", MODERATOR),
    )


class User(models.Model):
    first_name = models.CharField(verbose_name="Имя", help_text="Введите имя пользователя до 60 знаков", max_length=60)
    last_name = models.CharField(max_length=80)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    role = models.CharField(choices=UserRoles.choices, default='member', max_length=12)
    location = models.ManyToManyField(Location)
    age = models.PositiveIntegerField

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
