from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == 'POST':
        print(request.POST)
        listing_id = request.POST['listing_id']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(listing=listing, listing_id=listing_id, name=name, phone=phone,
                          user_id=user_id,  email=email,  message=message)
        contact.save()

        messages.success(request, 'Your inquiry has been submitted')

        return redirect('/listings/'+listing_id)