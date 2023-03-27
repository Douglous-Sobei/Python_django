from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/%Y/%m/%d")
    facebook_link = models.URLField(max_length=95)
    twitter_link = models.URLField(max_length=80)
    created_date = models.DateTimeField(auto_now_add=True)
    google_plus_link = models.URLField(max_length=85)

    def __str__(self):
        return self.first_name
    