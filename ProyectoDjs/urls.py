"""
URL configuration for ProyectoDjs project.

"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('panel/', include('panel.urls')),
]
