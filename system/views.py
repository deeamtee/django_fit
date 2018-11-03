from django.shortcuts import render


def index(request):
    template = 'user/index.html'
    context = {}
    return render(request, template, context)
