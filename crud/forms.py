from django import forms
from .models import eventModel

# form to be filled up
class eventForm(forms.ModelForm):
    class Meta:
        model = eventModel
        fields = ['event', 'total', 'description', 'pic']