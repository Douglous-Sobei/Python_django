from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review


# Create your views here.

class MyView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session["favorite_review"]
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
