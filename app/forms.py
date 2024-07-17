from .models import Customer
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomerForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = (
                "email",
                "first_name",
                "last_name",
                "password1",
                "password2",
            )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith("@gmail.com"):
            raise forms.ValidationError("Почта должна быть gmail!.")
        return email
