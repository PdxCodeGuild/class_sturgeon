from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, redirect, render
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.urls.base import reverse_lazy
from django .views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView, View, ListView
from django.contrib import messages
from posts.views import Post


# Create your views here.
class NewUser(CreateView):
    form_class = UserCreationForm
    template_name = 'new_user.html'
    success_url = reverse_lazy('login')

    

class UserProfileView(DetailView):
    model = User
    template_name = 'registration/profile.html'
    cotext_object_name = 'profile'
    

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

