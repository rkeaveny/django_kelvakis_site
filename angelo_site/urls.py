from django.contrib import admin
from django.urls import path
from inputs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('allbase/', views.allbase, name='allbase'),
    path('home/allbase/', views.allbase, name='allbase'),
    path('info/', views.info, name='info'),
]
