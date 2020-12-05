from django.urls import path
from .views import home

app_name = 'appweb'
urlpatterns = [
    path('', home, name='index'),
]