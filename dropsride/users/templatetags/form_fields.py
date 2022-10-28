from django import template
from django.forms import CheckboxInput, DateInput, Select, ClearableFileInput

register = template.Library()

@register.filter(name='is_checkbox')
def is_checkbox(field):
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__

@register.filter(name='is_date')
def is_date(field):
    return field.field.widget.__class__.__name__ == DateInput().__class__.__name__

@register.filter(name='is_select')
def is_select(field):
    return field.field.widget.__class__.__name__ == Select().__class__.__name__

@register.filter(name='is_file')
def is_file(field):
    return field.field.widget.__class__.__name__ == ClearableFileInput().__class__.__name__

