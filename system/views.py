from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def index(request):
    template = 'user/index.html'
    context = {}
    return render(request, template, context)


# def register(request):
#     form = UserCreationForm()
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
#             login(request, user)
#             return redirect('index')
#
#     template = 'account/register.html'
#     context = {'form': form}
#     return render(request, template, context)


def logout(request):
    template = 'user/index.html'
    context = {}
    return render(request, template, context)