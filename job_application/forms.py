# Import the forms module from django
from django import forms


# Define a new form named ApplicationForm
class ApplicationForm(forms.Form):
    # Define a character field named first_name with a maximum length of 80
    first_name = forms.CharField(max_length=80)
    # Define a character field named last_name with a maximum length of 80
    last_name = forms.CharField(max_length=80)
    # Define an email field named email
    email = forms.EmailField()
    # Define a date field named date
    date = forms.DateField()
    # Define a character field named occupation with a maximum length of 80
    occupation = forms.CharField(max_length=80)
