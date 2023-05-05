from django.shortcuts import render
from .forms import Imageform
from .models import Image

# Create your views here.

def index(request):
    if request.method =="POST":
        form=Imageform(request.POST,request.FILES)
        if form.is_valid:
            form.save()
    form=Imageform()
    img=Image.objects.all()
    return render(request,'Home/index.html',{'img':img,'form':form}  )