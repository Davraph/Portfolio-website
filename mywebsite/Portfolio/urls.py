from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='portfolios'),
    path('<int:portfolio_id>', views.portfolio, name='portfolio')
]
