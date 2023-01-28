from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def review(request):
    if request.method == 'POST':
        entered_username = request.POST['username']

        if entered_username == "":
            return render(request, "reviews/review.html", {
                "has_error": True
            })
        print(entered_username)
        return HttpResponseRedirect("/thank-you")
    
    return render(request, "reviews/review.html", {
        "has_error": False
    })

def thank_you(request):
    return render(request, "reviews/thanks.html")