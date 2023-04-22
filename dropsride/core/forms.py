from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, min_length=8)
    company = forms.CharField(max_length=500, min_length=5)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15, min_length=11)
    message = forms.CharField(widget=forms.Textarea())

    def clean_message(self):
        message = self.cleaned_data["message"]
        if len(message) <= 5:
            raise ValidationError(
                "Message is too short and has little to no information. Please write your concerns even clearer"
            )

        if "<script>" in message or "php" in message:
            raise ValidationError("Malicious script detected. Aborting now!")
        return message

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not phone.startswith("+"):
            raise ValidationError(
                "Please ensure to start with +[country code]. eg. +234"
            )
        return phone

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not "@" in email:
            raise ValidationError("a valid email must have @ sign within it")
        return email

    def clean_company(self):
        company = self.cleaned_data["company"]
        if len(company) <= 5:
            raise ValidationError(
                "Your company name is too short. Are you perhaps using acronyms?"
            )

        if "dropsride" in company:
            raise ValidationError("Are you trying to impersonate us?")
        return company

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) <= 6:
            raise ValidationError(
                "Your name is too short. Are you perhaps using acronyms?"
            )
        return name
