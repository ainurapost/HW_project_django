from django import forms
from .models import News
from django.core.exceptions import ValidationError
import re


inputAttrs = {
    'class': "form-control"
}


class NewNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'category', 'content']
        widgets = {
            'title': forms.TextInput(attrs=inputAttrs),
            'category': forms.Select(attrs=inputAttrs),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError("title can not begin with digit")
        return title


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs=inputAttrs))
    password = forms.CharField(widget=forms.PasswordInput(attrs=inputAttrs))
    firstName = forms.CharField(widget=forms.TextInput(attrs=inputAttrs))
    lastName = forms.CharField(widget=forms.TextInput(attrs=inputAttrs))
    email = forms.CharField(widget=forms.EmailInput(attrs=inputAttrs))


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs=inputAttrs)
    )
    password = forms.CharField(
        label='Password',
        max_length=64,
        widget=forms.PasswordInput(attrs=inputAttrs)
    )


class RatingForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['rating_sum']
