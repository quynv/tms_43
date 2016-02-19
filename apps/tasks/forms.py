from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'description': forms.Textarea(
                attrs={'rows': 15, 'class': 'form-control', 'style': 'resize:vertical;',
                    'placeholder': 'Write some thing...'}),
            'status': forms.Select(
                            attrs={'class': 'form-control selector', 'title': 'Status'})
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
