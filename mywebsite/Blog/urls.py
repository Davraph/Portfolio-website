from re import search
from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.StartingPageView.as_view(), name='blog'),
    path('<slug:slug>/', views.SinglePostView.as_view(), name='post-detail'),
]