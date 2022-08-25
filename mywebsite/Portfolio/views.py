from turtle import title
from django.shortcuts import render , get_object_or_404
from .models import Portfolio

# Create your views here.
def index(request):
    portfolios = Portfolio.objects.all()
    
    context = {
        'portfolios': portfolios,
    } 
    
    return render(request, 'pages/portfolio.html', context)


def portfolio(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    
    context = {
        'portfolio': portfolio
    }
    
    return render(request, 'pages/portfolio-detail.html', context)