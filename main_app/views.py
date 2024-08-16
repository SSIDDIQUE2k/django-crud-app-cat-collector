# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')