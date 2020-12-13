from django.urls import path
from .views import Aboutus

urlpatterns = [
    path('aboutus/', Aboutus, name="aboutus")
]