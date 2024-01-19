# Generated by Django 5.0.1 on 2024-01-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('current_vintage', models.CharField(max_length=50)),
                ('alcohol_volume', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=50)),
                ('brand_name', models.CharField(max_length=100)),
                ('wine_sweetness', models.CharField(max_length=50)),
                ('wine_body', models.CharField(max_length=50)),
                ('food_match', models.CharField(max_length=100)),
            ],
        ),
    ]
