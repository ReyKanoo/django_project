from django import forms
from .models import block
from django.contrib.auth.models import User
from .models import Profile

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

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'placeholder': 'dev123@rfss.ru'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '12345'}))
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': None,
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'dev123'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'dev123'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '12345'}))