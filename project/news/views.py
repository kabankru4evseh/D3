from django.shortcuts import render
from .models import New
from django.views.generic import ListView, DetailView


def index(request):
    news = New.objects.all()
    return render(request, 'index.html', context={'news': news})


def detail(request, slug):
    new = New.objects.get(slug__iexact=slug)
    return render(request, 'details.html', context={'new': new})


class NewList(ListView):
    model = New
    template_name = 'news.html'
    context_object_name = 'news'


class NewDetail(DetailView):
    model = New
    template_name = 'new.html'
    context_object_name = 'new'
