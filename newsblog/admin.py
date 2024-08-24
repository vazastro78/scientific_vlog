from django.contrib import admin
from newsblog.models import Article

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "body", "created_at", "updated_at", "is_visible", "view_counts")
    list_filter = ('is_visible',)
    search_fields = ('title', 'body',)
    