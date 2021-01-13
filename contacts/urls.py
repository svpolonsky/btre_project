from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('contact_owner', views.contact_owner, name='contact_owner'),
    #path('contact_owner_captcha', views.contact_owner_captcha, name='contact_owner_captcha'),
    path('request_from_prospect', views.request_from_prospect, name='request_from_prospect')
    
]