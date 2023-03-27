from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator

# Create your models here.

class Car(models.Model):
    
    state_choice = (
        ("BA", "Baringo"),
        ("BO", "Bomet"),
        ("BN", "Bungoma"),
        ("BS", "Busia"),
        ("EL", "Elgeyo marakwet"),
        ("EM", "Embu"),
        ("GA", "Garissa"),
        ("HO", "Homabay"),
        ("IS", "Isiolo"),
        ("KA", "Kajiado"),
        ("KK", "Kakamega"),
        ("KE", "Kericho"),
        ("KI", "Kiambu"),
        ("KL", "Kilifi"),
        ("KR", "Kirinyaga"),
        ("KS", "Kisii"),
        ("KU", "Kisumu"),
        ("KT", "Kitui"),
        ("KW", "Kwale"),
        ("LA", "Laikipia"),
        ("LM", "Lamu"),
        ("MA", "Machakos"),
        ("MK", "Makueni"),
        ("MN", "Mandera"),
        ("ME", "Meru"),
        ("MI", "Migori"),
        ("MR", "Marsabit"),
        ("MO", "Mombasa"),
        ("MU", "Muranga"),
        ("NA", "Nairobi"),
        ("NK", "Nakuru"),
        ("NN", "Nandi"),
        ("NR", "Narok"),
        ("NY", "Nyamira"),
        ("ND", "Nyandarua"),
        ("NE", "Nyeri"),
        ("SA", "Samburu"),
        ("SI", "Siaya"),
        ("TA", "Taita Taveta"),
        ("TN", "Tana River"),
        ("TH", "Tharaka Nithi"),
        ("TR", "Tra Nzoia"),
        ("TU", "Turkana"),
        ("UA", "Uasin Gishu"),
        ("VI", "Vihiga"),
        ("WA", "Wajir"),
        ("WE", "West Pokot"),
    )

    year_choices = [(r, r) for r in range(2005, datetime.now().year + 1)]

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=150)
    state = models.CharField(choices=state_choice, max_length=80)
    city = models.CharField(max_length=30)
    color = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    year = models.IntegerField(choices=year_choices)
    condition = models.CharField(max_length=150)
    price = models.IntegerField()
    description = RichTextField()
    car_image = models.ImageField(upload_to="images/%Y/%m/%d/")
    car_image_1 = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True)
    car_image_2 = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True)
    car_image_3 = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True)
    car_image_4 = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True)
    feature = MultiSelectField(choices=features_choices, validators=[MaxValueValidator(20)])
    body_style = models.CharField(max_length=90)
    engine = models.CharField(max_length=80)
    transmission = models.CharField(max_length=150)
    interior = models.CharField(max_length=150)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=9)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=75)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=30)
    no_of_owners = models.CharField(max_length=150)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField( blank=True, default=datetime.now)

    def __str__(self):
        return self.car_title