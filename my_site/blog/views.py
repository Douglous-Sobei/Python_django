from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "Hiking-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Douglous Mangoyi",
        "date": date(2023, 1, 18),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing  which is much great like the views you get when hiking in the mountains! And I wasn't even prepared for what happened but I was enjoying the view!",
        "content": """
          The mountain features were looking beatiful and very attractive. Both the rocks, trees and grass were some of the features that made the mountain to look great.

          The mountain's climate was cool. Had favorable weather conditions that made my hiking enjoyable. The fresh air made me feel relaxed and forgot about stress.

          Therefore, it is good to explore the world to discover its beatiful surroundings.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Douglous Mangoyi",
        "date": date(2023, 1, 19),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Programming is such a fun. It keeps the mind active and fresh than ever. 

          Because of its logical and real nature programming is one of the tools used to solve world's biggest problems in a critical way.
          
          I don't regret beaing a programmer because am part of the problem solvers.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Douglous Mangoyi",
        "date": date(2023, 1, 20),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
         There is freshness when having good time with nature since it entertaining and wonderful.

          Nature makes you explore the green vegetation which makes the world's physical appearance great.
          
          It is my liking to explore and have clear detail of what nature looks like.
        """
    }
]

def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })