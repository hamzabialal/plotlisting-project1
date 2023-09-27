from django.db import models

# Create your models here.
class Listings(models.Model):
    TYPE_CHOICES = [
        ('Car', 'Car'),
        ('Food and Life', 'Food and Life'),
        ('Travelling', 'Travelling'),
        ('Appartements', 'Appartements'),
        ('Shopping', 'Shopping'),

    ]

    area = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    price = models.IntegerField()
    image = models.ImageField(upload_to='shop/images', default="")
    title = models.CharField(max_length=170, default="")
    listing_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
class Mycontactform(models.Model):
    desc = models.TextField()
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
