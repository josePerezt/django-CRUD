from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import Login,Register,CreateTask
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
# Create your views here.

# Bienvenida
def welcome(request):
  return render(request,"welcome/index.html")


# Register de mi app
def signup(request):

  if request.method == "POST":
    usename = request.POST["username"]
    password1 = request.POST["password1"]
    password2 = request.POST["password2"]
    if password1 == password2:
      try:
        # se crea el usuario
        user = User.objects.create_user(username=usename,password=password1)
        # se guarda el usuario
        user.save()
      #  se envia un mensaje de exito al usuairo
        messages.success(request,"Usuario creado con exito")
        return redirect("login")
      except IntegrityError:
        messages.error(request,"El usuario ya existe")
        return render(request,"signup/index.html",{"form":Register()})
    else:
      messages.error(request,"Las contraseñas no coinciden")
      return render(request,"signup/index.html",{"form":Register()})
  else:
    return render(request,"signup/index.html",{"form":Register()})



# Login de mi app
def loging(request):
  if request.method == "POST":
    username= request.POST["username"]
    password = request.POST["password"]
    user_auth = authenticate(request,username=username,password=password)
  
    # validamos que el usuario exista
    if user_auth is not None:
      login(request,user_auth)
      return redirect("home")
    else:
      # sino obtenemos un usuario enviamos un mensaje de error y olvemos a mostrar el form
      messages.error(request,"El usuario y/o contraseña no existe")
      return render(request,"login/index.html",{"form":Login()})
  else:
    return render(request,"login/index.html",{"form":Login()})
  
# home de mi app
@login_required
def home(request):
  return render(request,"home/index.html") 


def signout(request):
  logout(request)
  return redirect("login")


def task(request):
  return render(request,"task/index.html")

def createTask(request):
  return render(request,"create_task/index.html",{
    "form":CreateTask
  })