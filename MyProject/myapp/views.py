from django.shortcuts import render
from myapp.models import  *
from myapp.forms import *
# Create your views here.

def index(request):
    x = Product.objects.all()
    return render(request, 'myapp/index.html', {'users': x,})


def addItens(request):
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'myapp/addItens.html',{'form': form})