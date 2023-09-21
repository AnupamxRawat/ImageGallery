from django.shortcuts import render
from .forms import Imageform,ImageUpdateForm
from .models import Image

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Image  # Import your Image model


# Create your views here.

def index(request):
    if request.method =="POST":
        form=Imageform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    form=Imageform()
    img=Image.objects.all()
    return render(request,'Home/index.html',{'img':img,'form':form}  )



def update_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)

    if request.method == 'POST':
        form = ImageUpdateForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the homepage after updating
    else:
        form = ImageUpdateForm(instance=image)

    return render(request, 'Home/update_image.html', {'form': form, 'image': image})

def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)

    if request.method == 'POST':
        if image.image:
            try:
                # Delete the image file from the media folder
                image.image.delete(save=True)
            except FileNotFoundError:
                messages.warning(request, 'File not found for this image.')
            # Delete the image record from the database
            image.delete()
            messages.success(request, 'Image deleted successfully.')
        else:
            messages.error(request, 'No file associated with this image.')

        return redirect('index')

    return render(request, 'Home/index.html')