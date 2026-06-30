from django import forms
from .models import block

class BlocksForm(forms.ModelForm):
    class Meta:
        model = block
        fields = ['title', 'description']

    def clean_title(self):
        title = self.cleaned_data['title']
        
        if len(title) < 3:
            raise forms.ValidationError('Название слишком короткое')
        
        if title[0].islower():
            raise forms.ValidationError('Название должно начинаться с заглавной буквы')
        
        return title  # обязательно вернуть значение
