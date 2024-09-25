from django.urls import path
from weather.views import WeatherViewSet

urlpatterns = [
    path('weathers/<str:city>/', WeatherViewSet.as_view(), name='weathers'),
]
