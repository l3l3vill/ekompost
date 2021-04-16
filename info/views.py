from django.shortcuts import render
from .models import Contact
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home_view(request):

    if request.method == 'POST':
        contact = Contact()

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.phone_number = phone
        contact.message = message

        contact.save()
        print('saveeeed')

        send_mail(
            name, message, settings.EMAIL_HOST_USER, [
                'greenprojectapp@gmail.com']
        )

        return HttpResponseRedirect(reverse('thanks_contact'))
    else:
        print('method not post')

    return render(request, "info/home.html")


def thanks_contact(request):

    return render(request, "info/thanks_contact.html")
