from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required

from . import utils

from .models import Wine
import csv
from io import TextIOWrapper
from pytrends.request import TrendReq

# Create your views here.
def home(request):
    cur_time = datetime.now()
    context = {}
    context['time'] = cur_time
    return render(request, 'myapp/homepage.html', context=context)


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
                    'food_match': row['Food Match'],
                    'rating': row['Rating']
                }
            )
        return HttpResponse("CSV file imported successfully")
    else:
        return render(request, 'myapp/import_csv.html')

# View for Model 2:To scrape the prices from 'https://www.danmurphys.com.au/list/wine?filters=country(italy)'


def recommendation(request):
    context = {'time': datetime.now()}
    if request.method == 'POST':
        selected_sweetness = request.POST["sweetness"]
        selected_vintage = request.POST["vintage"]
        selected_body = request.POST["body"]
        selected_pairing = request.POST["pairing"]
        selected_quantity = request.POST["quantity"]
        selected_alcohol_content = request.POST["alcohol_content"]
        print("selected sweetness is " + selected_sweetness)
        print("selected vintage is " + selected_vintage)
        print("selected_body is " + selected_body)
        print("selected pairing is " + selected_pairing)
        print("selected_alcohol_content is " + selected_alcohol_content)
        # call into database using filters
        recommended_wines = utils.get_wines(selected_sweetness, selected_vintage, selected_body, selected_pairing, selected_quantity, selected_alcohol_content)
        print(recommended_wines)
        return render(request, 'myapp/recommendation.html', {'my_list': recommended_wines})
    else:
        return render(request, 'myapp/recommendation.html', context=context)

      
def trending_view(request):
    selected_region = request.GET.get('region')  # Get the selected region from the request

    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = ["Cabernet Sauvignon", "Pinot Noir", "Chardonnay", "Merlot", "Sauvignon Blanc"]

    # Check if a region is selected, otherwise default to 'US'
    if not selected_region:
        selected_region = 'US'

    pytrends.build_payload(kw_list, cat=0, timeframe='today 3-m', geo=selected_region, gprop='')
    interest_over_time_df = pytrends.interest_over_time()

    # Dropping 'isPartial' column
    if 'isPartial' in interest_over_time_df.columns:
        interest_over_time_df = interest_over_time_df.drop('isPartial', axis=1)

    # Sum up and sort values to get top 3
    trending_wines = interest_over_time_df.sum().sort_values(ascending=False).head(3)

    context = {
        'selected_region': selected_region,
        'trending_wines': trending_wines.to_dict(),
    }
    return render(request, 'myapp/trending.html', context)

