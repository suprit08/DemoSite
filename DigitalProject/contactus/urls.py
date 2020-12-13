from django.urls import path
from .views import Contactus

urlpatterns = [
    path('', Contactus, name="contactus")
]