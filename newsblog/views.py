from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from pytils.translit import slugify
from django.urls import reverse_lazy, reverse

from newsblog.models import Article



# Create your views here.

def my_slugify( title, created_at ):
    return created_at.strftime("%Y%m%d-%H%M-") + slugify(title)


class ArticleListView(ListView):
    extra_context = {
        'title': 'Страница просмотра всех статей'
    }
    template_name = 'newsblog/artile_listallarticles.html'


    model = Article

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_visible=True)
        return queryset


class ArticleCreateView(CreateView):
    model = Article
    extra_context = {
        'title': 'Страница создания новой статьи'
    }
    fields = ("title", "slug", "body", "is_visible", "preview")
    template_name = 'newsblog/article_create_single.html'

    def get_success_url(self):
        return reverse_lazy('newsblog:listallarticles')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = my_slugify(new_article.created_at, new_article.title)
            new_article.save()
        return super().form_valid(form)

class ArticleDetailView(DetailView):
    model = Article
    extra_context = {
        'title': 'Страница просмотра отдельной статьи'
    }
    template_name = 'newsblog/article_view_single.html'
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counts += 1
        self.object.save()
        return self.object

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ( 'title', 'body', 'is_visible', 'preview' )
    template_name = 'newsblog/article_update_single.html'

    extra_context = {
        'title': 'Страница изменения отдельной статьи'
    }
    def get_success_url(self):
        return reverse_lazy('newsblog:view_single_article',args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = my_slugify(new_article.created_at, new_article.title)
            new_article.save()
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    model = Article
    extra_context = {
        'title': 'Страница удаления отдельной статьи'
    }
    template_name = 'newsblog/article_confirm_delete_single.html'
    def get_success_url(self):
        return reverse_lazy('newsblog:listallarticles')
