from django.shortcuts import render
from Portfolio.models import Portfolio


# Create your views here.
def home(request):
    portfolios = Portfolio.objects.all()
    
    context ={
        'portfolios': portfolios
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

