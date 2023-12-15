from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from listings.choices import bedroom_choices, price_choices, state_choices
from realtors.models import Realtor

def index(request):

    latest_listings = Listing.objects.order_by('-list_date')[:3]

    context = {
        'latest_listings': latest_listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.all()

    context = {
        'realtors': realtors
    }

    return render(request, 'pages/about.html', context)

def search(request):
    return render(request, 'listings/search')
