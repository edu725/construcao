from django import forms
from django.forms import ModelForm
from .models import Product
from .models import Order
from .models import ItemOrder

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name' : 'nome',
            'description': 'descricao',
            'price': 'preco',
            'image': 'imagem',
            'stock': 'estoque'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Saco de Cimento'
                }
            ),
            'descripion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Cimento'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: 150.00'
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: 10'
                }
            ),
            'image': forms.ClearableFileInput(),
        }