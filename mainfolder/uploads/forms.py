from django import forms
from .models import AssignmentUpload

class UploadForm(forms.ModelForm):
    class Meta:
        model = AssignmentUpload
        fields = ['file']
