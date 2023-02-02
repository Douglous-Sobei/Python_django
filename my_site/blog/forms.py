from django import forms
from .models import comment

class commentform(forms.ModelForm):
    class Meta:
        model = comment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment"
        }