from django.shortcuts import render
from django.core.mail import send_mail 
from django.core.mail import EmailMessage
from Makini.settings import EMAIL_HOST_USER

# Create your views here.
def index(request):
    return render(request,'index.html',{})



def contact(request):
    if request.method == "POST":
        message_name =  request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        # Send an email 

        send_mail(
            message_name,# subject 
            message, # message 
            message_email, # email 
            ['ondeyostephen0@gmail.com'], # To email 
        )
        return render(request,'contact.html',{'message_name':message_name})

    else:
        return render(request,'contact.html',{})