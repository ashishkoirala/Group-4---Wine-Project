from django.db import models

# Create your models here.

# Model 1: To upload the .csv file scrapped from 'https://www.danmurphys.com.au/list/wine?filters=country(italy)'

from django.db import models

class Wine(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_link = models.URLField(max_length=200, blank=True)
    quantity = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    current_vintage = models.CharField(max_length=50)
    alcohol_volume = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=100)
    wine_sweetness = models.CharField(max_length=50)
    wine_body = models.CharField(max_length=50)
    food_match = models.CharField(max_length=100)
    def __str__(self):
        return self.product_name