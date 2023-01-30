from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Reviewform
from .models import Review


# Create your views here.

def review(request):
    if request.method == 'POST':
        form = Reviewform(request.POST)
        if form.is_valid():
            my_review = Review(user_name=form.cleaned_data['user_name'], 
                               review_text=form.cleaned_data['review_text'], 
                               rating=form.cleaned_data['rating'])
            my_review.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = Reviewform()
    return render(request, "reviews/review.html", {
        "form": form
    })

def thank_you(request):
    return render(request, "reviews/thanks.html")