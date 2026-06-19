from django import forms
from .models import block

class BlockForm(forms.ModelForm):
    class Meta:
        model = block
        fields = ['title', 'description', 'is_done']
