from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


# Create your views here.
class SignUpView (CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def profile (request, username):
    user_profile = get_object_or_404(User, username=username)
    context = {
        'profile': user_profile,
        
    }
    return render(request, 'profile.html', context)
