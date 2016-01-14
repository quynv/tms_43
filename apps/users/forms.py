__author__ = 'javimuu'

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    MIN_LENGTH = 6
    MAX_LENGTH = 30

    class Meta:
        model = User
        fields = ("username","first_name", "last_name", "email", "password1", "password2")

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < self.MIN_LENGTH:
            raise ValidationError("The new password must be at least %d characters long." % self.MIN_LENGTH)

        if len(password1) > self.MAX_LENGTH:
            raise ValidationError("The new password must be less than %d characters long." % self.MAX_LENGTH)

        return password1

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class DocumentForm(forms.Form):
    avatar = forms.FileField(label='Change avatar',)