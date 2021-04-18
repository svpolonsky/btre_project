from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='owner_dashboard'),
    path('transactions/<int:period>', views.transactions, name='owner_transactions'),
    path('statement/<str:country>/<int:year>', views.statement, name='owner_statement')
]