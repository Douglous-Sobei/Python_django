from django import forms

class Reviewform(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=90, error_messages={
        "required": "Your name shouldn't be blank!",
        "max_length": "Please do not exceed the number of characters"
    })

    review_text = forms.CharField(label="Your Response", widget=forms.Textarea, max_length=250)
    rating = forms.IntegerField(label="You Rating", min_value=1, max_value=7)