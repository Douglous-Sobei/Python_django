from django import forms
from .models import Review

# class Reviewform(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=90, error_messages={
#         "required": "Your name shouldn't be blank!",
#         "max_length": "Please do not exceed the number of characters"
#     })

#     review_text = forms.CharField(label="Your Response", widget=forms.Textarea, max_length=250)
#     rating = forms.IntegerField(label="You Rating", min_value=1, max_value=7)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ['owner_comment']