# Import necessary modules from Django
from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages

# Import necessary modules for sending email
import smtplib
import ssl
import os

# Function to send custom email
def send_custom_email(message, receiver):
    # Define SMTP server details
    host = "smtp.gmail.com"
    port = 465
    username = "badboy27796@gmail.com"

    # Get the password from environment variable
    password = os.getenv("PASSWORD")
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Establish a secure connection with the server
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        # Login to the email account
        server.login(username, password)
        # Create the email message
        msg = f"Subject: New Application\n\n{message}"
        # Send the email
        server.sendmail(username, receiver, msg=msg)

# Function to handle the index page
def index(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Create a form instance and populate it with data from the request
        form = ApplicationForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Extract data from the form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            # Create a new Form object and save it to the database
            Form.objects.create(first_name=first_name, last_name=last_name, email=email, date=date,
                                occupation=occupation)

            # Create the email message
            message_body = f"A new job application was submitted!"
            # Send the email
            send_custom_email(message_body, email)

            # Show a success message
            messages.success(request, "Form submitted successfully")
    # Render the index page
    return render(request, "index.html")

# Function to handle the about page
def about(request):
    # Render the about page
    return render(request, 'about.html')