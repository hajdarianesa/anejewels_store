from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['category', 'name', 'quantity', 'price', 'description', 'image']
