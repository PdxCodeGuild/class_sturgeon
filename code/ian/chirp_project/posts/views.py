
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from posts.models import Comments, Post
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

# Create your views here.


class PostListView(ListView):
    model=Post
    template_name='home.html'

class PostDetailView(DetailView):
    model=Post
    template_name='details.html'




class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    template_name='new.html'
    fields=['title', 'body']
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    

    
class PostUpdateView(UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title', 'body']
    template_name='update.html'
    redirect_field_name = 'posts:details'
    
    
    def form_valid(self, form):
        messages.success(self.request, "You edited a post!")
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    
class PostDeleteView(UserPassesTestMixin, DeleteView):
    model=Post
    template_name='delete.html'
    success_url = reverse_lazy('posts:home')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# @csrf_protect     
def like(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        
        # new_data = Comments()
        # new_data.post_item = post
        # acct = request.user
        # print(acct)
        # new_data.users_liked.set(acct)
        
        # new_data.save()
        # print(post)
        # print(request.user)
        post.likes += 1
        post.save()
        context = {'post':post}
        return render(request, 'details.html', context)
    else: 
        return redirect(reverse_lazy('posts:home'))

