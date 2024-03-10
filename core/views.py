from django.shortcuts import render, redirect
from .forms import DogForm
from .models import Dog

def index(request):
    context = {'title':'Index', 'form':DogForm()}
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        context['form'] = form
    return render(request, 'index.html', context)

def list_dogs(request):
    dogs = Dog.objects.all()
    context = {'dogs':dogs}
    return render(request, 'list.html', context)
