from django import template
from django.forms import RadioSelect, ClearableFileInput

register = template.Library()

@register.filter(name='is_radio_select')
def is_radio_select(field_widget):
    return isinstance(field_widget, RadioSelect)

@register.filter(name='is_file_input')
def is_file_input(field_widget):
    return isinstance(field_widget, ClearableFileInput)
