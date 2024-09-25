from django.urls import path
from weather.views import WeatherViewSet
from django.shortcuts import redirect

def redirect_to_swagger(request):
    return redirect('/swagger/')

urlpatterns = [
    path('', redirect_to_swagger, name='home'),
    path('weathers/<str:city>/', WeatherViewSet.as_view(), name='weathers'),
]
