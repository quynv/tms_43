from django import forms
from django.contrib.auth.models import User
from apps.courses.models import Course
from apps.users.forms import UserCreateForm
from apps.courses.forms import CourseForm


class UserForm(UserCreateForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)

        if commit:
            user.is_supervisor = user.is_staff
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_staff']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'First name'}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Last name'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Email'}
            )
        }

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super(UserUpdateForm, self).save(commit=False)

        if commit:
            user.save()
        return user


class AdminCourseForm(CourseForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'status', 'supervisors']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'description': forms.Textarea(
                attrs={'rows': 10, 'class': 'form-control', 'style': 'resize:vertical;',
                    'placeholder': 'Write some thing...'}),
            'status': forms.Select(
                            attrs={'class': 'form-control selector', 'title': 'Status'}),
            'supervisors': forms.SelectMultiple(attrs={
                'class': 'form-control selectpicker', 'title': 'Add supervisors to this course'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(AdminCourseForm, self).__init__(*args, **kwargs)
        self.fields["supervisors"].widget.choices = [(user.id, user.username) for user in User.objects.filter(is_superuser=1,is_staff=1)]

