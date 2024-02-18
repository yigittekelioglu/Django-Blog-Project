from django import forms
from blog.models import Product, ImagesGal

class ProductForm(forms.ModelForm):
    image_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Product
        fields = ['product_title']
