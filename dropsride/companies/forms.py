from django import forms
from .models import CompanySavedAddress

class CompanyAddressForm(forms.ModelForm):
    address = forms.CharField(max_length=250, required=True, widget=forms.HiddenInput())
    city = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    post_code = forms.CharField(max_length=8, required=True, widget=forms.HiddenInput())
    state = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    country = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    latitude = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())
    longitude = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())

    class Meta:
        model = CompanySavedAddress
        fields = [
            'address_type',
            'address',
            'city',
            'post_code',
            'state',
            'country',
            'latitude',
            'longitude',
        ]



