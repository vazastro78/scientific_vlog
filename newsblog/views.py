from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from pytils.translit import slugify
from django.urls import reverse_lazy, reverse

from newsblog.models import Article


# Create your views here.


class ArticleListView(ListView):
    extra_context = {
        'title': 'Страница просмотра материалов'
    }
    template_name = 'newsblog/artile_listallarticles.html'


    model = Article
    '''

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset
    '''


class ArticleCreateView(CreateView):
    model = Article
    fields = ("title", "slug", "body", "is_visible", "preview")
    template_name = 'newsblog/article_create_single.html'

    def get_success_url(self):
        return reverse_lazy('newsblog:listallarticles')

    def form_valid(self, form):
        if form.is_valid():
            new_material = form.save()
            new_material.slug = slugify(new_material.title)
            new_material.save()
        return super().form_valid(form)
