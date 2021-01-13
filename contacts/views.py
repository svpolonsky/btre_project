from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Contact, ContactOwner
from .forms import ContactForm


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




def request_from_prospect(request):
    if request.POST:
        form = ContactForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            # human = True
            r = form.save(commit=False)
            # assume the user is not registered 
            r.user_id = 0
            r.save()
            # inform admin by email about the inquiry
            try:
                subject='YouMoscow Inquiry'
                context= ({"name": r.name, "email":r.email, "phone":r.phone,"message":r.message})
                text_content = render_to_string('owner_inquiry.txt', context, request=request)
                html_content = render_to_string('owner_inquiry.html', context, request=request)
                emailOfSender= settings.EMAIL_HOST_USER
                emailOfRecipient = 'spolonsky@icloud.com' 
                #I used EmailMultiAlternatives because I wanted to send both text and html
                emailMessage = EmailMultiAlternatives(
                    subject=subject, 
                    body=text_content, 
                    from_email=emailOfSender, 
                    to=[emailOfRecipient,], 
                    reply_to=[emailOfSender,])
                emailMessage.attach_alternative(html_content, "text/html")
                emailMessage.send(fail_silently=False)
                messages.success(request, 'You request has been submitted, a realtor will get back to you soon.')
            except:
                messages.warning(request, 'Cannot email confirmation')
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'contacts/request_from_prospect.html', {'form': form})


def contact_owner(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        # record an inquiry from a potential owner
        contact_owner = ContactOwner(name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact_owner.save()
        # inform admin by email about the inquiry
        try:
            subject='YouMoscow Inquiry'
            context= ({"name": name, "email":email, "phone":phone,"message":message})
            text_content = render_to_string('owner_inquiry.txt', context, request=request)
            html_content = render_to_string('owner_inquiry.html', context, request=request)
            emailOfSender= settings.EMAIL_HOST_USER
            emailOfRecipient = 'spolonsky@icloud.com' 
            #I used EmailMultiAlternatives because I wanted to send both text and html
            emailMessage = EmailMultiAlternatives(
                subject=subject, 
                body=text_content, 
                from_email=emailOfSender, 
                to=[emailOfRecipient,], 
                reply_to=[emailOfSender,])
            emailMessage.attach_alternative(html_content, "text/html")
            emailMessage.send(fail_silently=False)
            messages.success(request, 'You request has been submitted, a realtor will get back to you soon.')
        except:
            messages.warning(request, 'Cannot email confirmation')
        return redirect('index')

import smtplib

def sendEmail():
    # so far, I couldn't get this working.
    # MS requires oauth and this is difficult for me to implement
    #import smtplib

    mailserver = smtplib.SMTP('smtp.office365.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login('stas@youmoscow.com', '8gYbAz44yZD')
    mailserver.sendmail('stas@youmoscow.com', 'spolonsky@icloud.com','python email')
    mailserver.quit()

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login('stas@youmoscow.com', '8gYbAz44yZD')

    try:
        server.sendmail('stas@youmoscow.com', 'spolonsky@icloud.com', 'messageBeingSent')
    except:
        print('An error occurred when trying to send an email')

    server.quit()
