import time
from .models import CustomUser
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .forms import UserRegisterForm

def customUser(request):
  custom_user = CustomUser.objects.get(id = 1)

  context = {
    'codigoUDG': custom_user.codigoUDG,
    'email': custom_user.get_rol_display(),
  }

  return render(request, 'profile.html', context)

def login_user(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    # Intentar autenticar con CustomUser
    user_custom = authenticate(request, username=username, password=password)

    # Si la autenticación con CustomUser falla, intentar con User predeterminado
    if user_custom is None:
      user_default = authenticate(request, username=username, password=password)

      # Si la autenticación con User predeterminado también falla, mostrar un mensaje de error
      if user_default is None:
        return JsonResponse({'success': False, 'message': 'Nombre de usuario o contraseña incorrectos.'})

      # Si la autenticación con User predeterminado tiene éxito, iniciar sesión y responder con éxito
      login(request, user_default)
      return JsonResponse({'success': True, 'message': 'Inicio de sesión exitoso.'})

    # Si la autenticación con CustomUser tiene éxito, iniciar sesión y responder con éxito
    login(request, user_custom)
    return JsonResponse({'success': True, 'message': 'Inicio de sesión exitoso.'})

  else:
    return render(request, 'authenticate/login.html')

@login_required(login_url='login')
def logout_user(request):
  logout(request)
  return redirect('login')

# @login_required(login_url='login')
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.rol == 'Jefe de Departamento':
                user.is_superuser = True
                user.is_staff = True
                user.save()
                
                # Agregar permisos para acceder al panel de administración
                permissions_to_assign = [
                    'view_customuser',  # Reemplaza 'customuser' con el nombre de tu modelo si es diferente
                    # Agrega más permisos según sea necesario para otros modelos
                ]
                for permission_code in permissions_to_assign:
                    permission = Permission.objects.get(codename=permission_code)
                    user.user_permissions.add(permission)
            else:
                user.save()
            return redirect('register_user')
    else:
        form = UserRegisterForm()
    time.sleep(1.5)

    return render(request, 'authenticate/register_user.html', {
        'form': form
    })

@login_required(login_url='login')
def profile(request):
  return render(request, 'profile.html')