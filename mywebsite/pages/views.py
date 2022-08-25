from turtle import title
from django.shortcuts import render
from Portfolio.models import Portfolio


# Create your views here.
def home(request):
    portfolios = Portfolio.objects.order_by('created_on')[:2]

    context ={
        'portfolios': portfolios
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

