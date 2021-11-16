
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Registration_form


def register(request):
    if request.method == 'POST':
        form = Registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can log in.')
            return redirect('login')
    else:
        form = Registration_form()
    return render(request, 'users/register.html', {'form': form})

