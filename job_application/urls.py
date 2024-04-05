# Import necessary modules
from django.urls import path
from . import views

# Define URL patterns
urlpatterns = [
    # Map the root URL ('') to the index view
    path('', views.index, name='index'),
    # Map the 'about/' URL to the about view
    path('about/', views.about, name='about')]