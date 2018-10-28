from django.urls import path, include
from .views import index, register, logout, profile_data

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('index/', index),
    path('register/', register),
    path('logout/', logout),
    path('profile/', profile_data),

]
