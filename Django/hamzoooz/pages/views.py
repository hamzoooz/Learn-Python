from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse('Hello Worled ')
# def index(request):
#     return HttpResponse('Hello Worled ')

def about(request):
    return HttpResponse('Hello Worled ')

def index(request):
    a = {
        "name" : "hamzoooz",
        "Age" : 23
    }
    return render(request, 'pages/index.html', a )
