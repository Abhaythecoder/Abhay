from django.urls import path
from . import views

urlpatterns = [
    # This is the portfolio view from before
    path('', views.portfolio_view, name='home'), 
    
    # This is the new path for the contact form
    path('contact/', views.contact_view, name='contact'), 
]