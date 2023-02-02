from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from . models import Post
from .forms import commentform

# Create your views here.

class StartPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class allpostsview(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

class singlepostview(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = commentform()
        return context
