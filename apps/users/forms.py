__author__ = 'javimuu'

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserCreateForm(UserCreationForm):
    MIN_LENGTH = 6
    MAX_LENGTH = 30

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm password'}))


    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Username'}
            ),
            'first_name': forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'First name'}
            ),
            'last_name': forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Last name'}
            ),
            'email': forms.EmailInput(
                attrs={'class':'form-control', 'placeholder':'Email'}
            ),
            'password1':forms.PasswordInput(
                attrs={'class':'form-control', 'placeholder':'Password'}
            ),
            'password2':forms.PasswordInput(
                attrs={'class':'form-control', 'placeholder':'Password'}
            ),
        }


    # def clean_password1(self):
    #     password = self.cleaned_data.get('password1')
    #     # confirmation = self.cleaned_data.get('password2')
    #
    #     if len(password) < self.MIN_LENGTH:
    #         raise ValidationError("The new password must be at least %d characters long." % self.MIN_LENGTH)
    #
    #     if len(password) > self.MAX_LENGTH:
    #         raise ValidationError("The new password must be less than %d characters long." % self.MAX_LENGTH)
    #
    #     return self.cleaned_data


    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True
        self.fields['password1'].required = True


class DocumentForm(forms.Form):
    avatar = forms.FileField(label='Change avatar',)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'First name'}
            ),
            'last_name': forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Last name'}
            ),
            'email': forms.EmailInput(
                attrs={'class':'form-control', 'placeholder':'Email'}
            ),
        }
