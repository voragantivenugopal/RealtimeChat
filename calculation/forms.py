from django import forms
from django.forms.widgets import TextInput
from simpleeval import simple_eval

from .models import RealEditor


class EditorForm(forms.ModelForm):
    class Meta:
        model = RealEditor
        fields = ['message']
        widgets = {
            'Input': TextInput(attrs={'autocomplete': 'off'}),
        }

    def is_valid(self):

        valid = super(EditorForm, self).is_valid()

        if not valid:
            return valid

        try:
            self.cleaned_data['message']
            return True
        except:
            self._errors['invalid_exp'] = 'Invalid message'
            return False
