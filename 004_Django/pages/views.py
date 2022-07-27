from django.shortcuts import render
from .models import Login 
from .forms import LoginForm
# from .models import  pages

# # Create your views here.
def index(request):
    return render(request, 'pages/index.html' )

def about(request):
    def __str__(self):
        return self.username        

    username = request.POST.get('username')
    password = request.POST.get('password')
    
    data = Login(username=username, password=password)
    
    if request.method == 'POST':
        if data.is_valid():
            data.save()


    # return render(request, 'pages/about.html' )
    return render(request, 'pages/about.html' )

def singup(request):
    
    data = LoginForm(request.POST)
    if request.method == 'POST':
        if data.is_valid():
            data.save()
            
    return render(request, 'pages/singup.html', {'lf':LoginForm} )

    # def __str__(self):
    #     return self.username        
