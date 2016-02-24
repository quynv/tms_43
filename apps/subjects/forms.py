from django import forms
from apps.subjects.models import Subject
from apps.subjects.models import Course

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'description', 'status', 'course']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'description': forms.Textarea(
                attrs={'rows': 15, 'class': 'form-control', 'style': 'resize:vertical;',
                    'placeholder': 'Write some thing...'}),
            'status': forms.Select(
                            attrs={'class': 'form-control selector', 'title': 'Status'}),
            'course': forms.SelectMultiple(
                            attrs={'class': 'form-control multiselect', 'title': 'Select course'})
        }

    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        self.fields['course'].widget.choices = [(course.id, course.name) for course in Course.objects.all()]
