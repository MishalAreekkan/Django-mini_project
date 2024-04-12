from django.urls import path
from . import views
urlpatterns = [
    path("",views.signin,name="signin"),
    path("login",views.login,name="login"),
    path("home",views.home,name="home"),
    path("list",views.listed,name="list"),
] 