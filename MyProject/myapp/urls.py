from django.urls import path
from myapp.views import *

# Create your views here.

urlpatterns = [
    path("", index, name="index"),
]