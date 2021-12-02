from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Post

# Create your views here.

class ChirpListView (ListView):
    model = Post
    template_name = 'home.html'

class ChirpDetailView (DetailView):
    model = Post
    template_name = 'detail.html'

class ChirpCreateView (CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['chirp']
    success_url = reverse_lazy('posts:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ChirpDeleteView (DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('posts:home')
