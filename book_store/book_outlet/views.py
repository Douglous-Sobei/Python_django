from django.shortcuts import render, get_object_or_404
from . models import My_books
from django.http import Http404
from django.db.models import Avg

# Create your views here.

def index(request):
    my_books = My_books.objects.all().order_by("title")
    number_of_books = my_books.count()
    avg_rating = my_books.aggregate(Avg("rating"))

    return render(request, "book_outlet/index.html", {
        "my_books": my_books,
        "overal_number_of_books":number_of_books,
        "average_rating": avg_rating
    })

def book_detail(request, slug):
    # try:
        # book = My_books.objects.get(pk=id)
    # except:
        # raise Http404() 
    book = get_object_or_404(My_books, slug=slug)  
    return render(request, "book_outlet/book_detail.html", {
      "title": book.title,
      "author": book.author,
      "rating": book.rating,
      "is_bestseller": book.is_bestselling  
    })