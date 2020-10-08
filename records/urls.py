from django.urls import path

from . import  views

urlpatterns = [
    path('cvsreport/<int:unit_id>', views.report_unit, name='report_unit')
]

