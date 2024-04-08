from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("women website")


def about(request):
    return HttpResponse("about")