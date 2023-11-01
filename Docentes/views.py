import time
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .forms import UserRegisterForm

def login_user(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return JsonResponse({'success': True})
    else:
      return JsonResponse({'success': False, 'message': 'Hubo un error al iniciar sesión, inténtalo de nuevo...'})

  else:
    return render(request, 'authenticate/login.html')

@login_required(login_url='login')
def logout_user(request):
  logout(request)
  return redirect('login')

@login_required(login_url='login')
def register_user(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(request, username=username, password=password)
      login(request, user)
      time.sleep(1.5)
      return redirect('inicio')
  
  else:
    form = UserRegisterForm()

  return render(request, 'authenticate/register_user.html', {
    'form': form
  })

@login_required(login_url='login')
def profile(request):
  return render(request, 'profile.html')