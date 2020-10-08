from django.shortcuts import render, get_object_or_404
from .models import Owner
from listings.models import Listing as Unit
from records.models import Expense, Revenue


def dashboard(request):
    # user -> owner -> units -> records
    # user to owner
    owner=get_object_or_404(Owner, user=request.user)
    # owner to properties
    units = Unit.objects.filter(owner=owner)
    expenses = Expense.objects.filter(unit__in=units)
    revenues = Revenue.objects.filter(unit__in=units)
    context = {
        'owner': owner,
        'units': units,
        'expenses': expenses,
        'revenues': revenues
    }
    return render(request,'owners/dashboard.html', context)
