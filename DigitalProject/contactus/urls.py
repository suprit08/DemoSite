from django.urls import path
from .views import Contactus

urlpatterns = [
    path('contactus/', Contactus, name="contactus")
]