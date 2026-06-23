from django import forms
from .models import block

class BlocksForm(forms.ModelForm):
    class Meta:
        model = block
        fields = ['title', 'description']
