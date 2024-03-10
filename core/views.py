from django.shortcuts import render
from .forms import DogForm

def index(request):
    context = {'title':'Index', 'form':DogForm()}
    return render(request, 'index.html', context)