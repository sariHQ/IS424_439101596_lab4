from django.shortcuts import render
from django.http import HttpResponse


def default_view(request):
    return render(request, 'tax_app/default.html')


def calculate_tax_view(request, price):
    tax_rate = 0.15  # Tax rate as a decimal
    total_price = price + (price * tax_rate)
    return HttpResponse(f'Total price with tax: {total_price}')


def tax_rate_view(request):
    tax_rate = 0.15  # Tax rate as a decimal
    return render(request, 'tax_app/tax_rate.html', {'tax_rate': tax_rate})
