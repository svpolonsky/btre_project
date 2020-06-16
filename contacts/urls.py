from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('contact_owner', views.contact_owner, name='contact_owner')
    
]