from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartPageView.as_view(), name="starting-page"),
    path("posts", views.allpostsview.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.singlepostview.as_view(), name="post-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]
