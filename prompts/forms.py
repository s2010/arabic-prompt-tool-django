# prompts/forms.py
from django import forms
from .models import Prompt

class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ['title', 'content'] # Fields users can submit
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}), # Make content a textarea
        }
