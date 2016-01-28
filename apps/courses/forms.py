from django import forms
from .models import Course
from apps.subjects.models import Subject


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'description': forms.Textarea(
                attrs={'rows': 15, 'class': 'form-control', 'style': 'resize:vertical;',
                    'placeholder': 'Write some thing...'}),
        }

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'description': forms.Textarea(
                attrs={'rows': 15, 'class': 'form-control', 'style': 'resize:vertical;',
                    'placeholder': 'Write some thing...'}),
        }

    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
