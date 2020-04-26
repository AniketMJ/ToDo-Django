from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
        labels = {
            'text': ''
        }
        widgets = {
            'text': forms.TextInput(attrs={'autocomplete': 'off', 'autofocus': 'on'})
        }
