from django.contrib import admin

from django.contrib import admin
from .models import Wine
import csv
from io import TextIOWrapper

# Register your models here.

# Registering Model 1: To upload the .csv file scrapped from 'https://www.danmurphys.com.au/list/wine?filters=country(italy)'

@admin.action(description='Import wines from a CSV file')
def import_csv(modeladmin, request, queryset):
    for obj in queryset:
        with open(obj.csv_file.path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Wine.objects.create(
                    product_name=row['Product Name'],
                    quantity=row['Quantity'],
                    type=row['Type'],
                    size=row['Size'],
                    region=row['Region'],
                    current_vintage=row['Current Vintage'],
                    alcohol_volume=row['Alcohol Volume'],
                    country=row['Country'],
                    brand_name=row['Brand Name'],
                    wine_sweetness=row['Wine Sweetness'],
                    wine_body=row['Wine Body'],
                    food_match=row['Food Match'],
                    rating=row['Rating'],
                )

class WineAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'type', 'brand_name')
    actions = [import_csv]

admin.site.register(Wine, WineAdmin)