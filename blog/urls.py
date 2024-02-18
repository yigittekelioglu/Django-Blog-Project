from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list/<slug:slug>/', views.list, name='list'),
    path('catalog/', views.catalog, name='catalog'),
    path('details/<slug:slug>/', views.details, name='details'),
    path('moviedetails/<slug:slug>/', views.moviedetails, name='moviedetails'),
    path('castdetails/<slug:slug>/', views.castdetails, name='castdetails'),
]