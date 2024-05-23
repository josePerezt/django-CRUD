from typing import Any
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.forms import ModelForm
from .models import Task



class Login(AuthenticationForm):
  def __init__(self, *args ,**kwargs):
    super().__init__( *args, **kwargs)
    self.fields["username"].widget.attrs.update({
      "class":"login",
      "placeholder":"ingresa tu usuario"
    })
    self.fields['username'].label = ''
    self.fields["password"].widget.attrs.update({
      "class":"login",
      "placeholder":"Ingresa tu contraseña"
    })
    self.fields["password"].label= ""
    
class Register(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields["username"].widget.attrs.update({
      "class":"register",
      "placeholder":"ingresa tu contraseña"
    })
    self.fields["password1"].widget.attrs.update({
      "class":"register",
      "placeholder":"Ingrese su contraseña"
    })
    self.fields["password2"].widget.attrs.update({
      "class":"register",
      "placeholder":"confirme su contraseña"
    })
    self.fields["username"].label = ""
    self.fields["password1"].label = ""
    self.fields["password2"].label = ""
    

class CreateTask(ModelForm):
  class Meta:
    model= Task
    fields=["title","description","important"]
  