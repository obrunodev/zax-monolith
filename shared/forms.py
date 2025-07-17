# seu_app/forms.py

from django import forms

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        default_input_classes = 'form-control'
        
        widgets_to_style = (
            forms.TextInput, forms.NumberInput, forms.EmailInput, 
            forms.URLInput, forms.PasswordInput, forms.Textarea, 
            forms.Select, forms.DateInput, forms.DateTimeInput, 
            forms.TimeInput
        )
        
        for field_name, field in self.fields.items():
            if isinstance(field.widget, widgets_to_style):
                current_classes = field.widget.attrs.get('class', '')
                new_classes = ' '.join(sorted(list(set(current_classes.split() + default_input_classes.split()))))
                field.widget.attrs['class'] = new_classes
            
            if isinstance(field.widget, (forms.TextInput, forms.NumberInput, forms.EmailInput, forms.URLInput, forms.PasswordInput)):
                if not field.widget.attrs.get('placeholder') and field.label:
                    field.widget.attrs['placeholder'] = field.label

            if isinstance(field.widget, forms.DateInput):
                field.widget.attrs['type'] = 'date'
            elif isinstance(field.widget, forms.DateTimeInput):
                field.widget.attrs['type'] = 'datetime-local'
            elif isinstance(field.widget, forms.TimeInput):
                field.widget.attrs['type'] = 'time'

            if isinstance(field.widget, forms.ClearableFileInput):
                current_classes = field.widget.attrs.get('class', '')
                file_input_classes = 'form-control'
                new_classes = ' '.join(sorted(list(set(current_classes.split() + file_input_classes.split()))))
                field.widget.attrs['class'] = new_classes
