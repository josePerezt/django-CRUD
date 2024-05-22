from django.urls import path
from . import views


urlpatterns=[
  path("",views.welcome, name="welcome"),
  path("signup/",views.signup,name="signup"),
  path("login/",views.loging, name="login"),
  path("home/",views.home, name="home"),
  path("logout/",views.signout,name="logout"),
  path("task/",views.task, name="task"),
  path("task/create",views.createTask, name="create_task")
]

