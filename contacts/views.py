from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from .models import Contact, ContactOwner

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        send_mail(
            'Property listing inquiry',
            'There has been an inquiry for '+listing+'. Sign into the admin panel for more info',
            'svpolonsky@gmail.com',
            [realtor_email, 'svpolonsky@outlook.com'],
            fail_silently=False
        )
        messages.success(request, 'You request has been submitted, a realtor will get back to you soon.')
        return redirect('/listings/'+listing_id)


def contact_owner(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        contact_owner = ContactOwner(name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact_owner.save()
        try:
            subject='test subject'
            body='test body'
            email_msg = EmailMessage(
                subject, 
                body, 
                settings.EMAIL_HOST_USER, 
                ['spolonsky@icloud.com'], 
                reply_to=[settings.EMAIL_HOST_USER]
                )    
            email_msg.send()
            messages.success(request, 'You request has been submitted, a realtor will get back to you soon.')
        except:
            messages.warning(request, 'Cannot email confirmation')
        return redirect('index')

""" import smtplib

def sendEmail():

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login('stas@youmoscow.com', '8gYbAz44yZD')

    try:
        server.sendmail('stas@youmoscow.com', 'spolonsky@icloud.com', 'messageBeingSent')
    except:
        print('An error occurred when trying to send an email')

    server.quit()
 """