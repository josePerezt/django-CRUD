from django.urls import path
from . import views


urlpatterns=[
  path("",views.welcome, name="welcome"),
  path("signup/",views.signup,name="signup"),
  path("login/",views.loging, name="login"),
  path("home/",views.home, name="home"),
  path("logout/",views.signout,name="logout"),
  path("task/",views.task, name="task"),
  path("task/detail/<int:task_id>",views.task_detail, name="task_detail"),
  path("task/create",views.createTask, name="create_task"),
  path("task/update/<int:task_id>",views.update_task, name="update_task"),
  path("task/delete/<int:task_id>",views.task_delete, name="task_delete"),
  path("task/completed/<int:task_id>",views.task_completed, name="task_completed")
]

