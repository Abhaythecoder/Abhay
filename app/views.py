from django.shortcuts import render
from django.http import HttpResponse

def portfolio_view(request):
    return render(request, 'app/index.html')
    
# Add this new function
def contact_view(request):
    return render(request, 'app/contact.html')