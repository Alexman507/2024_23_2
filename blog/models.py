from django.db import models
from django.utils import timezone

NULLABLE = {"blank": "True", "null": "True"}


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="заголовок")
    slug = models.CharField(max_length=150, verbose_name='URL', **NULLABLE)
    content = models.TextField(verbose_name="содержимое", **NULLABLE)
    preview = models.ImageField(upload_to='blog/photo', **NULLABLE, verbose_name='Превью')
    created_at = models.DateField(default=timezone.now, auto_created=True, verbose_name="дата создания")
    published = models.BooleanField(default=True, verbose_name='опубликован')
    views = models.IntegerField(default=0, verbose_name='просмотры')
