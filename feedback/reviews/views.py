from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Review


# Create your views here.

class MyView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
        "form": form
    })
    
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        
        return render(request, "reviews/review.html", {
        "form": form
    })

class ThankYouView(TemplateView):
    template_name = "reviews/thanks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This is workable!"
        return context
    
class ReviewListView(ListView):
    template_name = "reviews/review-list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=2)
    #     return data

class SingleReviewView(DetailView):
    template_name = "reviews/single-review.html"
    model = Review
