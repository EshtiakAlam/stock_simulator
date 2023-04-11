from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserProfileCreationForm
from .models import UserProfile

from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@transaction.atomic
def register(request):
    if request.method == 'POST':
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            user, created = form.save(commit=False)
            user.save()
            national_id = form.cleaned_data.get('national_id')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            UserProfile.objects.create(
                user=user,
                national_id=national_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                date_of_birth=date_of_birth,
            )
            login(request, user)
            return redirect('login')
    else:
        form = UserProfileCreationForm()
    return render(request, 'registration/register.html', {'form': form})
