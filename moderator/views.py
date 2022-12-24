from django.shortcuts import render, redirect
from submission.models import Confession
from moderator.models import Advert
from django.contrib.auth.decorators import login_required
import smtplib
from email.mime.text import MIMEText

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
    password = "rnwyvtugeziiqyyr"
    receipient = advert.email
    message = MIMEText(f"Dear {advert.name},\nWe are pleased to accept your request to advertise with our company. We believe that our platform will be a great fit for your business, and we are excited to help you reach your marketing goals. To get started, please provide us with the following information:\n- A brief description of your business and the products or services you offer The type of ad you would like to run (e.g. banner ad, sponsored post, etc.)\n- The target audience for your ad (e.g. age, gender, location, etc.)\n- The desired start and end dates for your ad campaign.\nOnce we have this information, we will create a customized advertising plan for your business and provide you with a detailed proposal. We look forward to working with you and helping you achieve success with your advertising efforts.\n\nSincerely,\nAdmin - TweetWave")
    message['Subject'] = "Advertising with TweetWave"
    message['From'] = "edgarmatthew247@gmail.com"
    message['To'] = advert.email
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    print('Login success')
    server.sendmail(sender, receipient, message.as_string())
    print('Confirmation email to ', receipient , ' has been sent')
    server.quit()
    advert.contacted = True
    advert.save()
    return redirect('moderator:adverts')


@login_required()
def reject(request, uuid):
    advert = Advert.objects.get(uuid=uuid)
    advert.delete()
    return redirect('moderator:adverts')


