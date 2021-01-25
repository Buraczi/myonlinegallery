from django.shortcuts import render
from django.http import HttpResponseRedirect # , HttpResponse
# from django.template import loader
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from .models import Image
from .forms import ImageUploadForm

class ImagePhoto(TemplateView):
    form = ImageUploadForm
    template_name = 'gallery/image_photo.html'

    def post(self, request, *args, **kwargs):
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():

            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('image_photo_display', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

from django.views.generic import DetailView
from .models import Image

class ImagePhotoDisplay(DetailView):
    model = Image
    template_name = 'gallery/image_photo_display.html'
    context_object_name = 'image'
    