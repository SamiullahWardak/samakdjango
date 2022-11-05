from django.shortcuts import get_object_or_404
from .ModelForm import BlogForm
from django.urls import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView
)

from .models import Article

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    #queryset = Article.objects.all()
    
    def get_object(self):
        _id = self.kwargs.get("pk")
        return get_object_or_404(Article, pk = _id)
    
class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = BlogForm
    queryset = Article.objects.all()
    
    def form_valid(self, form):
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = BlogForm
    
    def get_object(self):
        _id = self.kwargs.get("pk")
        return get_object_or_404(Article, pk = _id)
    
    def form_valid(self, form):
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    form_class = BlogForm

    def get_object(self):
        _id = self.kwargs.get("pk")
        return get_object_or_404(Article, pk = _id)
    
    def get_success_url(self):
        return reverse('articles:article-list')