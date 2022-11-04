from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=60, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Ad(models.Model):
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    name = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    price = models.PositiveBigIntegerField()
    description = models.TextField(null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='ads')

    def __str__(self):
        return self.name