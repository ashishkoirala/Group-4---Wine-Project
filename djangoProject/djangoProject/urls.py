"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.views import wine_preferences


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('winedb/import/', views.import_csv, name='import_csv'),
    path('preferences/', views.wine_preferences, name='wine_preferences'),
    path('recommendations/', views.wine_recommendation, name='wine_recommendation'),
]