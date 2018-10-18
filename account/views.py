from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.views.generic import TemplateView
from django.views.generic.base import View

from .forms import EmailPostForm


class LoginView(TemplateView):
    template_name = 'registration/login.html'

    def login(request):
        username = request.POST['username']
        password = request.POST['password']
        print('Получил username и password!')
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            print('Я тут был!')
            # Правильный пароль и пользователь "активен"
            auth.login(request, user)
            # Перенаправление на "правильную" страницу
            return HttpResponseRedirect("/registration/loggedin/")
        else:
            print('Ошибка! но тут был!')
            # Отображение страницы с ошибкой
            return HttpResponseRedirect("/registration/invalid/")


def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("/registration/loggedout/")


def testform(request):  # Retrieve post by id
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
    else:
        form = EmailPostForm()
    return render(request, 'registration/testform.html', {'form': form})
