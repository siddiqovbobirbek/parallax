from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from .models import *
from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'home.html', context)