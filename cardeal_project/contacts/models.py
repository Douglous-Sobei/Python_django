from django.db import models
from datetime import datetime

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    phone = models.CharField(max_length=80)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=80)
    car_title = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email