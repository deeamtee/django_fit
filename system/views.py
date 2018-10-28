from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from system.forms import ProfileForm
from system.models import Profile


def index(request):
    template = 'user/index.html'
    context = {}
    return render(request, template, context)


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            Profile.objects.create(**{
                'first_name': "first_name", 'last_name': 'last_name', 'age': 12
            })
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)


            return redirect('index')

    template = 'registration/register.html'
    context = {'form': form}
    return render(request, template, context)


def logout(request):
    template = 'user/index.html'
    context = {}
    return render(request, template, context)


# @login_required
# @transaction.atomic
def profile_data(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    context = {'profile_form': profile_form}
    return render(request, 'profiles/profile.html', context)
