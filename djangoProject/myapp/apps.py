from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

class TrendsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trends'