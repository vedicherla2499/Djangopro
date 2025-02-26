from django.urls import path
from myapp import views

urlpatterns = [
    path("home/",views.home_func,name="home"),
    path("http/",views.http_func,name="http"),
]
