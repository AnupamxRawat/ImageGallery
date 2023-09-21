from django import forms
from .models import Image

class Imageform(forms.ModelForm):
    class Meta:
        model=Image
        fields='__all__'
        labels={'image':''}


class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']  

class ImageSearchForm(forms.Form):
    image_id = forms.IntegerField(label='Image ID')        