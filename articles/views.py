from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView

# Create your views here.
class Articledetail(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'art'
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
class Articleupdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    fields = ['title','body', 'photo']
    template_name = 'article_update.html'

    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user
class Articledelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj=self.get_object()
        return obj.author == self.request.user
class Articlecreate(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ['title', 'summery','body','photo']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

