from django import forms

class Reviewform(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=90, error_messages={
        "required": "Your name shouldn't be blank!",
        "max_length": "Please do not exceed the number of characters"
    })