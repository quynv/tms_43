from django import forms
from django.contrib.auth.models import User
from apps.users.forms import UserCreateForm


class UserForm(UserCreateForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff']
        widgets = {
            "is_superuser": forms.Select(
                        attrs={'class': 'form-control selectpicker', 'title': 'Select type of user'},
                        choices=([(0, 'Trainee'), (1, 'Supervisor')])),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        if commit:
            user.is_staff = user.is_superuser
            user.save()
        return user

