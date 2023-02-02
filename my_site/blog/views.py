from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from . models import Post
from .forms import commentform
from django.views import View

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

class singlepostview(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment": commentform()
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment = commentform(request.POST)
        post = Post.objects.get(slug=slug)

        if comment.is_valid():
            Comment = comment.save(commit=False)
            Comment.post = post
            Comment.save()
            
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment": commentform
        }
        return render(request, "blog/post-detail.html", context) 