from django import forms
from django.contrib.auth.models import User
from apps.reports.models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(
                            attrs={'class': 'form-report-title form-control', 'placeholder': 'Title'}),
            'content': forms.Textarea(
                            attrs={'rows': 50, 'class': 'form-report-content form-control', 'style': 'resize:vertical;',
                                   'placeholder': 'Write some thing...'}),
            'tags': forms.SelectMultiple(
                            attrs={'class': 'form-control selectpicker', 'title': 'Tag someone'})
        }

    def __init__(self, *args, **kwargs):
        # self.user = kwargs.pop('User', None)
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields['tags'].widget.choices = [(user.id, user.username) for user in User.objects.all()]
        self.fields['title'].required = True
        self.fields['content'].required = True


