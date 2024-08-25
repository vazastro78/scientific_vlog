from django.contrib import admin
from newsblog.models import Article

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "slug", "view_counts",  "created_at", "updated_at", "is_visible" )
    fields = ("title", "body", "preview", "is_visible" )
    list_filter = ('is_visible', 'title')
    search_fields = ('title', 'body',)

