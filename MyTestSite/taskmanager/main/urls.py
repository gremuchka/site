from django.urls import path
from . import views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('register', user_views.register, name='register'),
    path('profile', user_views.ShowProfilePageView.as_view(), name='profile'),

    # login|logout parts; paths
    path('login', user_views.log, name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]
