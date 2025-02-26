from django.contrib import admin
from django.urls import path

from myproj.urls import urlpatterns

# Register your models here.

urlpatterns = [
    path('/admin',admin.site.urls),
]
