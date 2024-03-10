from django.shortcuts import render, redirect, get_object_or_404
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
    context = {'title':'Dogs list', 'dogs':dogs}
    return render(request, 'list.html', context)

def delete(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    dog.delete()
    return redirect('dogs')