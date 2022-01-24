from django.shortcuts import render, get_object_or_404,redirect
from datetime import datetime
from .models import Post, User
from django.template import loader
from django.contrib.auth.decorators import login_required


def landing(request):
    if request.method == 'POST':
        print(request.POST) 
        data = dict(request.POST)
        print(data)
        body=request.POST.get('words')
        Post.objects.create(
			body=body,
			time=datetime.now(),
            author=request.user,
		)
        return redirect('/')

    context={'posts':(Post.objects.all()),}
    print(context)
    return render(request, 'chirp/landing.html', context)

@login_required
def delete(request, id):
    item = get_object_or_404(Post, id=id)
    item.delete()
    return redirect('posts:landing')

@login_required
def profile(request, id):
    if request.method == 'POST':
        print(request.POST) 
        data = dict(request.POST)
        print(data)
        body=request.POST.get('words')
        Post.objects.create(
			body=body,
			time=datetime.now(),
            author=request.user,
		)
        return redirect('/user')
    user=get_object_or_404(User, id=id)
    context={'posts':(Post.objects.filter(author=user.id))}
    return render(request, 'chirp/user.html', context)