from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.


def inquiry(request):
    if request.method == "POST":
        car_id = request.POST["car_id"]
        car_title = request.POST["car_title"]
        user_id = request.POST["user_id"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        customer_need = request.POST["customer_need"]
        city = request.POST["city"]
        state = request.POST["state"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        if request.user.is_authenticated:
            user_id = request.user.id
            made_contact = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if made_contact:
                messages.error(
                    request, "You have already made an inquiry, we will get back to as soon as request is processed.")
                return redirect("/cars/"+car_id)

        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id,
                          first_name=first_name, last_name=last_name, customer_need=customer_need,
                          city=city, state=state, email=email, phone=phone, message=message)
        admin_detail = User.objects.get(is_superuser=True)
        admin_email = admin_detail.email
        send_mail(
            "New Car Inquiry",
            "You have an inquiry for the car " + car_title +
            ". Kindly login to your admin panel for more details.",
            "douglousmangoyi@gmail.com",
            [admin_email],
            fail_silently=False,
        )

        contact.save()
        messages.success(
            request, "Your message is successfully submitted, we will shortly get back to you.")
        return redirect("/cars/"+car_id)
