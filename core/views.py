from django.shortcuts import render

def index(request):
    context = {'title':'Index'}
    return render(request, 'index.html', context)