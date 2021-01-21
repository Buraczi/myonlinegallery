from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from django.template import loader

def index(request):
    images_in_order = Image.objects.order_by('-pub_date')[:10]
    template = loader.get_template('gallery/index.html')
    context = {
        'images_in_order': images_in_order,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.