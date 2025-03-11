from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Image
from .forms import ImageForm

@login_required
def image_list(request):
        images = Image.objects.all()
        return render(request, 'imagenes/image_list.html', {'images': images})


@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
         form.save()
        return redirect('image_list')
    else:
        form = ImageForm()
    
    return render(request, 'imagenes/upload_image.html', {'form': form})



# Create your views here.
