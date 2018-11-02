from django.urls import path, include
from system.views import index, register, logout, login

urlpatterns = [
    path('', include('allauth.urls')),
    # path('', include('django.contrib.auth.urls')),
    path('index/', index),

]
