from django.shortcuts import render, get_object_or_404
from .models import Owner
from listings.models import Listing as Unit
from records.models import Expense, Revenue
from records.filters import ExpenseFilter
from django.db.models import Sum
from datetime import datetime, timedelta
from .tables import LedgerTable
from django_tables2 import RequestConfig
from django.db.models.functions import TruncMonth, ExtractMonth
from django.db.models import Sum
from itertools import groupby


def dashboard(request):
    # user -> owner -> units -> records
    # user to owner
    owner=get_object_or_404(Owner, user=request.user)
    # owner to properties
    units = Unit.objects.filter(owner=owner)
    # per-property summaries
    
    last_month = datetime.today() - timedelta(days=30)
    last_year = datetime.today() - timedelta(days=365)
    data = [ 
        {
            "name": u.title,
            "revenue30d": Revenue.objects.filter(unit=u).filter(date__gte=last_month).aggregate(Sum('amount')).get('amount__sum', 0.00),
            "expense30d": Expense.objects.filter(unit=u).filter(date__gte=last_month).aggregate(Sum('amount')).get('amount__sum', 0.00),
            "profit30d":0.0,
            "revenue12m": Revenue.objects.filter(unit=u).filter(date__gte=last_year).aggregate(Sum('amount')).get('amount__sum', 0.00),
            "expense12m": Expense.objects.filter(unit=u).filter(date__gte=last_year).aggregate(Sum('amount')).get('amount__sum', 0.00),
            "profit12m":0.0
        } 
        for u in units]
    # compute profits
    for d in data:
        try:
            d["profit30d"]=d["revenue30d"]-d["expense30d"]
        except:
            d["profit30d"]=None
        try:
            d["profit12m"]=d["revenue12m"]-d["expense12m"]
        except:
            d["profit12m"]=None


    expenses = Expense.objects.filter(unit__in=units)
    revenues = Revenue.objects.filter(unit__in=units)
    


    expenses_filter = ExpenseFilter(request.GET, queryset=expenses)
    

    context = {
        'owner': owner,
        'summary':data,
        'units': units,
        'filter': expenses_filter,
        'expenses': expenses,
        'revenues': revenues
    }
    return render(request,'owners/dashboard.html', context)

def transactions(request,period):
    # period: days
    # user -> owner -> units -> records
    # user to owner
    owner=get_object_or_404(Owner, user=request.user)
    # owner to units
    units = Unit.objects.filter(owner=owner)
    duration = datetime.today() - timedelta(days=period)

    fields=['date','amount','category__category','unit__title','note']
    transactions = list(Expense.objects.filter(unit__in=units).filter(date__gte=duration).values(*fields))
    for t in transactions:
        t['amount']=-t['amount']
    transactions.extend(
        list(Revenue.objects.filter(unit__in=units).filter(date__gte=duration).values(*fields))
    )
    context={
        'ledger': RequestConfig(request).configure(LedgerTable(transactions))
    }
    return render(request,'owners/transactions.html', context)

def statement_helper(qs):
    # pivot table
    key_row='category__category'
    key_col='month'
    totals = qs \
        .annotate(month=ExtractMonth('date')) \
        .values(key_row,key_col) \
        .annotate(total=Sum('amount')) \
        .order_by(key_row,key_col)

    trow = [0] * 13 # monthly totals, [0] is YTD
    ctrows=[] # categorized  totals
    for category, group in groupby(totals, lambda x: x[key_row]):
        ctrow=[0] * 13 # [0] is YTD
        for e in group:
            ctrow[e[key_col]] = e['total']
            trow[e[key_col]] += ctrow[e[key_col]]
        ctrow[0]=sum(ctrow[1:]) # compute YTD
        ctrows.append([category] + ctrow)
    trow[0] = sum(trow[1:]) # YTD
    return trow,ctrows

def statement(request,country,year):
    # user -> owner -> units -> records
    # user to owner
    owner=get_object_or_404(Owner, user=request.user)
    # owner to properties
    units = Unit.objects.filter(owner=owner,country=country)
    # Income
    inc,cinc=statement_helper(Revenue.objects.filter(unit__in=units).filter(date__year=year))

    fields=['date','amount','category__category','unit__title']

    # Expense
    exp,cexp=statement_helper(Expense.objects.filter(unit__in=units).filter(date__year=year))
    
    # Net Operating Income
    noi = [i-e for i, e in zip(inc, exp)]

    context={
        'incomes': inc,
        'categorized_incomes': cinc,
        'expenses': exp,
        'categorized_expenses': cexp,
        'nets': noi
    }
    return render(request,'owners/statement.html', context)