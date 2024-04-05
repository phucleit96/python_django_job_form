# Import the models module from django.db
from django.db import models

# Define a new model named Form
class Form(models.Model):
    # Define a character field named first_name with a maximum length of 80
    first_name = models.CharField(max_length=80)
    # Define a character field named last_name with a maximum length of 80
    last_name = models.CharField(max_length=80)
    # Define an email field named email
    email = models.EmailField()
    # Define a date field named date
    date = models.DateField()
    # Define a character field named occupation with a maximum length of 80
    occupation = models.CharField(max_length=80)

    # Define the string representation of the model
    def __str__(self):
        # Return the first name and last name of the form applicant
        return f"{self.first_name} {self.last_name}"