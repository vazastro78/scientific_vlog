from django.db import models
from django.utils.timezone import now
from pytils.translit import slugify


def my_slugify( title, created_at ):
    return created_at.strftime("%Y%m%d-%H%M-") + slugify(title)

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=110, verbose_name='название')
    #slug_value = my_slugify(title.value_to_string, now())
    slug = models.CharField(max_length=160, unique=True, verbose_name='slug')
    body = models.TextField(verbose_name='заметка')
    view_counts = models.IntegerField(default=0, verbose_name='просмотры')
    preview = models.ImageField(upload_to="blog_thumbnail",verbose_name='превью')
    created_at = models.DateTimeField(verbose_name='дата создания',default=now, editable=False)
    updated_at = models.DateTimeField(verbose_name='дата изменения',default=now, editable=True)
    is_visible = models.BooleanField(default=True, verbose_name='видимость')

    def save(self, *args, **kwargs):
        self.slug = my_slugify( self.title, now())
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} {self.slug}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

