# Generated by Django 5.1 on 2024-08-24 20:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('slug', models.CharField(max_length=120, verbose_name='slug')),
                ('body', models.TextField(verbose_name='заметка')),
                ('preview', models.ImageField(upload_to='blog_thumbnail', verbose_name='превью')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата изменения')),
                ('is_visible', models.BooleanField(default=True, verbose_name='видимость')),
                ('view_counts', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]
