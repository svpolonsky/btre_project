import csv
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Revenue,Expense
from listings.models import Listing


# Create your views here.
def report_unit(request, unit_id):
    # Filter Revenue and Expense by unit_id, write to csv
    unit = get_object_or_404(Listing, pk=unit_id)
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="somename.csv"'
    writer=csv.writer(response)
    revenues=Revenue.objects.filter(unit=unit)
    for r in revenues:
        writer.writerow([r.date.strftime('%Y-%m-%d'),r.category,r.amount])
    expenses=Expense.objects.filter(unit=unit)
    for e in expenses:
        writer.writerow([e.date.strftime('%Y-%m-%d'),e.category,-e.amount]) 
    return response
