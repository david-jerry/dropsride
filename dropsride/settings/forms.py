from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox, ReCaptchaV3
from django import forms

from dropsride.settings.models import CarType, Localization


class LocalizationForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = Localization
        fields = [
            "state",
            "tiket_fare",
            "base_price",
            "cost_per_km",
            "cost_per_15min",
        ]


class CartypeForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = CarType
        fields = [
            "image",
            "title",
            "amount",
            "seats",
        ]
