from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}

    return render(request, 'newsblog/main.html', context)
#    return render(request, 'mainapp/index.html', context)

