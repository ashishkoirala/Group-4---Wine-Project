
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from .models import Wine
import csv
from io import TextIOWrapper


# Create your views here.
def home(request):
    cur_time = datetime.now()
    context = {}
    context['time'] = cur_time
    return render(request, 'myapp/homepage.html', context=context)

# View for Model 1:To upload the .csv file scrapped from 'https://www.danmurphys.com.au/list/wine?filters=country(italy)'

@staff_member_required
def import_csv(request):
    if request.method == 'POST':
        csv_file = TextIOWrapper(request.FILES['csv_file'].file, encoding='utf-8')
        reader = csv.DictReader(csv_file)
        for row in reader:
            Wine.objects.get_or_create(
                product_name=row['Product Name'],
                defaults={
                    'quantity': row['Quantity'],
                    'price': row['Price'],
                    'product_link': row['Product Link'],
                    'type': row['Type'],
                    'size': row['Size'],
                    'region': row['Region'],
                    'current_vintage': row['Current Vintage'],
                    'alcohol_volume': row['Alcohol Volume'],
                    'country': row['Country'],
                    'brand_name': row['Brand Name'],
                    'wine_sweetness': row['Wine Sweetness'],
                    'wine_body': row['Wine Body'],
                    'food_match': row['Food Match']
                }
            )
        return HttpResponse("CSV file imported successfully")
    else:
        return render(request, 'myapp/import_csv.html')

# View for Model 2:To scrape the prices from 'https://www.danmurphys.com.au/list/wine?filters=country(italy)'
