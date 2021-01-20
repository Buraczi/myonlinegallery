from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

def index(request):
    return HttpResponse("Index response test!")

# Create your views here.
# testing branches and marge