from django.contrib import admin
from Home.models import Image
# Register your models here.


class Adminimage(admin.ModelAdmin):
    list_display=['id','image','date']
admin.site.register(Image,Adminimage)
