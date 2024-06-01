from django import forms
from django.forms import ModelForm
from myapp.models import  *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name' : 'Nome',
            'dedescription': 'Descrição',
            'price': 'Preço',
            'image': 'Imagem',
            'stock': 'Estoque'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Saco de Cimento'
                }
            ),
            'dedescripion': forms.TextInput(
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