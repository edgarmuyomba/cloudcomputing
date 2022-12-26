from django.shortcuts import render, redirect
from .models import Confession
from moderator.models import Advert

def index(request):
    context = {}
    return render(request, 'submission/index.html', context)

def saved(request):
    if request.method == 'POST':
        tweet = request.POST['tweet']
        try:
            media = request.FILES['attachment']
        except:
            media = None
        newTweet = Confession(text=tweet, media=media)
        newTweet.save()
        return redirect('submission:index')

def advertising(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        company = request.POST['company']
        message = request.POST['message']
        newConfession = Advert(name=name, email=email, company=company, description=message)
        newConfession.save()
        return redirect('submission:index')
    context = {}
    return render(request, 'submission/advertising.html', context)

def business(request):
    context = {}
    return render(request, 'submission/business.html', context)

def about(request):
    context = {}
    return render(request, 'submission/about.html', context)
