from django import forms
from .models import article

class articleForm(forms.ModelForm):
    class Meta:
        model = article
        fields = [
            'title',
            'source',
        ]
