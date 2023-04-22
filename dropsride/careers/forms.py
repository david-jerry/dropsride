from django import forms
from django.forms import ModelForm
from django_select2 import forms as s2forms

from dropsride.settings.models import Localization

from .models import Applicants, Careers, Teams


class DepartmentForm(ModelForm):
    class Meta:
        model = Teams
        fields = ["title"]


class LocalizationWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "state__state__icontains",
    ]


class CareersForm(ModelForm):
    class Meta:
        model = Careers
        fields = [
            "title",
            "summary",
            "keywords",
            "team",
            "location",
            "salary",
            "competency",
            "content",
            "published_date",
            "draft",
        ]
        widgets = {
            "location": LocalizationWidget,
        }

    def clean_title(self):
        data = self.cleaned_data["title"]
        if len(data) <= 4:
            raise forms.ValidationError("Title is too small")
        return data

    def clean_summary(self):
        data = self.cleaned_data["summary"]
        if data == "":
            raise forms.ValidationError("Summary is required for SEO.")
        elif len(data) < 25:
            raise forms.ValidationError(
                "News Summary must be at least 25 characters long."
            )
        return data

    def clean_keywords(self):
        data = self.cleaned_data["keywords"]
        if data == "":
            raise forms.ValidationError("Keywords is required for SEO.")
        elif " , " not in data:
            raise forms.ValidationError(
                "This field must contain a comma. This is a list of keywords to be used for SEO."
            )
        return data

    def clean_location(self):
        data = self.cleaned_data["location"]
        if len(data) < 1:
            raise forms.ValidationError(
                "There must be a location for applicants to work in"
            )
        return data

    def clean_team(self):
        data = self.cleaned_data["team"]
        if data == None:
            raise forms.ValidationError("The team or department must be set")
        return data


class ApplicantsForm(ModelForm):
    class Meta:
        model = Applicants
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "phone_number",
            "gender",
            "age",
            "location",
            "file",
            "cover_letter",
            "disability",
            "consent",
            "country",
        ]

    def clean_first_name(self):
        data = self.cleaned_data["first_name"]
        if len(data) < 3:
            raise forms.ValidationError("This name is too short")
        return data

    def clean_middle_name(self):
        data = self.cleaned_data["middle_name"]
        if len(data) < 3:
            raise forms.ValidationError("This name is too short")
        return data

    def clean_last_name(self):
        data = self.cleaned_data["last_name"]
        if len(data) < 3:
            raise forms.ValidationError("This name is too short")
        return data
