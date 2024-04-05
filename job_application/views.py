from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages

import smtplib
import ssl
import os


def send_custom_email(message, receiver):
    host = "smtp.gmail.com"
    port = 465
    username = "badboy27796@gmail.com"

    password = os.getenv("PASSWORD")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        msg = f"Subject: New Application\n\n{message}"
        server.sendmail(username, receiver, msg=msg)


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            Form.objects.create(first_name=first_name, last_name=last_name, email=email, date=date,
                                occupation=occupation)

            message_body = f"A new job application was submitted!"
            send_custom_email(message_body, email)

            messages.success(request, "Form submitted successfully")
    return render(request, "index.html")

def about(request):
    return render(request, 'about.html')