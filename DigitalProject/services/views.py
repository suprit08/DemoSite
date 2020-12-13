from django.shortcuts import render

# Create your views here.
def Services(request):
    return render(request, 'services.html')