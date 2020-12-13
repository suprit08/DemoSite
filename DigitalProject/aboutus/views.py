from django.shortcuts import render

# Create your views here.
def Aboutus(request):
    return render(request, 'about.html')