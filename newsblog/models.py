from django.db import models
from django.utils.timezone import now

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    slug = models.CharField(max_length=120, verbose_name='slug')
    body = models.TextField(verbose_name='заметка')
    preview = models.ImageField(upload_to="blog_thumbnail",verbose_name='превью')
    created_at = models.DateTimeField(verbose_name='дата создания',default=now, editable=False)
    updated_at = models.DateTimeField(verbose_name='дата изменения',default=now, editable=True)
    is_visible = models.BooleanField(default=True, verbose_name='видимость')
    view_counts = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title} {self.created_at} {self.view_counts}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

