import django_filters
from django.shortcuts import get_object_or_404
from owners.models import Owner
from .models import Revenue,Expense
from listings.models import Listing

def ownerunits(request):
    if request is None:
        return Listing.objects.all()
    owner=get_object_or_404(Owner, user=request.user)
    return Listing.objects.filter(owner=owner)


class ExpenseFilter1(django_filters.FilterSet):
    # experiment with callable
    listing = django_filters.ModelChoiceFilter(queryset=ownerunits)
    class Meta:
        model = Expense
        fields = ['listing']

class ExpenseFilter(django_filters.FilterSet):
    unit__title = django_filters.CharFilter(lookup_expr='icontains',label='Property title')
    date = django_filters.DateRangeFilter(label='duration')
    class Meta:
        model = Expense
        fields = ['unit__title', ]