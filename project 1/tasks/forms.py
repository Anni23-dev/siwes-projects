# to build the submission engine. This handles automatic data capture and validation
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

    # Custom validation rule: Prevent empty titles or spam
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Task title must be at least 5 characters long!")
        return title
