import json

import requests
from django.shortcuts import render

from .models import Contact


def index(request):
    if request.method == 'POST':

        r = requests.get('https://xkcd.com/info.0.json')
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('img')

        context = {'joker': joke}
        return render(request, 'mysite/index.html', context)
    else:
        firstname = 'Attreya'
        lastname = 'Bhatt'

        r = requests.get('https://xkcd.com/info.0.json')
        json_data = json.loads(r.text)
        joke = json_data.get('img')

        context = {'joker': joke}
        return render(request, 'mysite/index.html', context)


def portfolio(request):
    return render(request, 'mysite/portfolio.html')


def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'mysite/thank.html')
    else:
        return render(request, 'mysite/contact.html')
