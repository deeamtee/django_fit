from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('test/', testform)
]
