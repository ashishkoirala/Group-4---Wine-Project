
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required

from .forms import WinePreferenceForm
from .models import Wine
import csv
from io import TextIOWrapper
from pytrends.request import TrendReq
from django.shortcuts import render

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
                    'food_match': row['Food Match'],
                    'rating': row['Rating']
                }
            )
        return HttpResponse("CSV file imported successfully")
    else:
        return render(request, 'myapp/import_csv.html')

# View for Model 2:To collect user preferences and give recommendations

def wine_preferences(request):
    form = WinePreferenceForm()
    return render(request, 'myapp/wine_preferences.html', {'form': form})

def wine_recommendation(request):
    if request.method == 'POST':
        form = WinePreferenceForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            # ... other form data ...
            alcohol_query = form.cleaned_data.get('alcohol_content')

            # Fetch all wines
            wines = Wine.objects.all()

            # Convert wines QuerySet to list for Python-side processing
            wines_list = list(wines)

            # Define a function to strip the '%' and convert to float
            def parse_alcohol_volume(wine):
                try:
                    return float(wine.alcohol_volume.strip('%'))
                except ValueError:
                    return None

            # Filter by alcohol content in Python
            def alcohol_filter(wine):
                alcohol_percentage = parse_alcohol_volume(wine)
                if alcohol_percentage is None:
                    return False  # Skip wines with invalid alcohol_volume data
                if alcohol_query == '<8':
                    return alcohol_percentage < 8
                elif alcohol_query == '8-15':
                    return 8 <= alcohol_percentage <= 15
                elif alcohol_query == '>15':
                    return alcohol_percentage > 15
                return True  # Include all wines if no specific alcohol query is selected

            wines_filtered = [wine for wine in wines_list if alcohol_filter(wine)]

            # ... other filters ...
            # Apply sweetness, body, and food filters on wines_filtered

            # Get the top-rated wines separately
            top_rated_wines = sorted(wines_filtered, key=lambda wine: wine.rating, reverse=True)[:3]

            # Render the recommendations page
            return render(request, 'myapp/wine_recommendations.html', {
                'wines': wines_filtered,
                'top_rated_wines': top_rated_wines
            })

    else:
        return wine_preferences(request)

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