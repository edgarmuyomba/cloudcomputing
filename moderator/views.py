from django.shortcuts import render, redirect
from submission.models import Confession
from moderator.models import Advert
from django.contrib.auth.decorators import login_required
import smtplib

def countFlags():
    flags = Confession.objects.all().filter(flag=True)
    return len(flags)

@login_required()
def index(request):
    confessions = Confession.objects.all()
    context = {'confessions': confessions, 'number': countFlags()}
    return render(request, 'moderator/index.html', context)

@login_required()
def approve(request, uuid):
    confession = Confession.objects.get(uuidField=uuid)
    confession.approved = True
    confession.save()
    return redirect('moderator:pending')

@login_required()
def remove(request, uuid):
    confession = Confession.objects.get(uuidField=uuid)
    confession.delete()
    return redirect('moderator:pending')

@login_required()
def approved(request):
    confessions = Confession.objects.all().filter(approved=True)
    context = {'confessions': confessions, 'number': countFlags()}
    return render(request, 'moderator/approved.html', context)


@login_required()
def pending(request):
    confessions = Confession.objects.all().filter(approved=False)
    context = {'confessions': confessions, 'number': countFlags()}
    return render(request, 'moderator/pending.html', context)

@login_required()
def flagged(request):
    flags = Confession.objects.all().filter(flag=True)
    number = len(flags)
    context = {'flags': flags, 'number': number}
    return render(request, 'moderator/flagged.html', context)

@login_required()
def adverts(request):
    adverts = Advert.objects.all()
    context = {'adverts': adverts, 'number': countFlags()}
    return render(request, 'moderator/adverts.html', context)

@login_required()
def contact(request, uuid):
    advert = Advert.objects.get(uuid=uuid)
    sender = "edgarmatthew247@gmail.com"
    receipient = advert.email
    subject = "Advertising with TweetWave"
    body = f"""Dear {advert.name}, <br> We are pleased to accept your request to advertise with our company. We believe that our p <br> latform will be a great fit for your business, and we are excited to help you reach your marketing goals. <br> To get started, please provide us with the following information: <br> A brief description of your business and the products or services you offer <br> The type of ad you would like to run (e.g. banner ad, sponsored post, etc.) <br> The target audience for your ad (e.g. age, gender, location, etc.) <br> The desired start and end dates for your ad campaign <br> Once we have this information, we will create a customized advertising plan for your business and provide you  <br> with a detailed proposal. We look forward to working with you and helping you achieve success with your advertising efforts. <br> Sincerely, <br> Admin - TweetWave"""
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.sendmail(sender, receipient, subject, body)


@login_required()
def reject(request, uuid):
    advert = Advert.objects.get(uuid=uuid)
    advert.delete()
    return redirect('moderator:adverts')


