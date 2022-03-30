from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from engforfuture import settings


def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
# Create your views here.
def email(request):
    subject = "Newsletter"
    message = "Mail sent"
    recipient = request.POST.get('email')
    send_mail(subject, message,settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
    return HttpResponse("mail sent")