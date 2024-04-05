# Import necessary modules
from django.contrib import admin
from .models import Form


# Define a new admin class named FormAdmin
class FormAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the list view
    list_display = ("first_name", "last_name", "email", "date", "occupation")
    # Define the fields to be searched in the search box
    search_fields = ("first_name", "last_name", "email")
    # Define the fields to be used in the filter sidebar
    list_filter = ("date", "occupation")
    # Define the default sorting field
    ordering = ("first_name",)
    # Define the fields to be read-only in the form view
    readonly_fields = ("occupation",)


# Register the Form model with the admin site using the FormAdmin class
admin.site.register(Form, FormAdmin)
