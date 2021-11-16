from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm
from users.models import Profile
from itertools import chain


# LoginRequired into Views because we don't want interlopers and non otoku in here
class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    context_object_name = 'form'

    # Add both a user and a profile to context, and yes, it needs those weird kwargs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context

class PostFeedView(ListView):
    """Return all published posts."""
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 10
    context_object_name = 'posts'


class PostDetailView(DetailView):
    """Detail view posts"""
    template_name = 'posts/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    queryset = Post.objects.all()
    context_object_name = 'post'

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.username
            comment.save()
            return HttpResponseRedirect(reverse('posts:detail', args=(post.pk,)))
    else:
        print("hello")
        form = CommentForm()
        return render(request, 'posts/add_comment_to_post.html', {'form': form})


def delete_own_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_add = comment.post.id
    comment.delete()
    return HttpResponseRedirect(reverse('posts:detail', args=(post_add,)))


#an idea on how to sort following posts
def posts_of_following_profiles(request):
    #login to profile
    profile = Profile.objects.get(user=request.user)
    #see who we're following
    users = [user for user in profile.following.all()]
    #initial values for variables
    posts = []
    qs = None
    #pull posts of people we follow
    for u in users:
        p = Profile.objects.get(user=u)
        p_posts = p.post_set.all()
        posts.append(p_posts)
    # our posts
    my_posts = profile.profiles_posts()
    posts.append(my_posts)
    #sort
    if len(posts)>0:
        qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)
    return render(request, 'posts/feed.html', {'posts': qs})