import requests
from datetime import date, datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from weatherforecast import settings
import json
import redis

# Kết nối Redis
r = redis.Redis(
    host='redis-15593.c295.ap-southeast-1-1.ec2.redns.redis-cloud.com',
    port=15593,
    password='Ao9Fky1wJBslnvgaELL0t7h4WPoopFHM'
)


class WeatherViewSet(APIView):
    PAGE_SIZE = 4

    def get(self, request, city):
        WEATHER_API_KEY = settings.WEATHER_API_KEY
        url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={city}&days=14"

        # Kiểm tra trong Redis trước
        cache_key = f"weather_{city}_{date.today().strftime('%Y-%m-%d')}"
        cached_data = r.get(cache_key)

        if cached_data:
            forecast_data = json.loads(cached_data)
        else:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                forecast_data = {
                    "city": data["location"]["name"],
                    "forecasts": []
                }

                for forecast in data["forecast"]["forecastday"]:
                    forecast_data["forecasts"].append({
                        "date": forecast["date"],
                        "temperature": forecast["day"]["avgtemp_c"],
                        "condition": forecast["day"]["condition"],
                        "wind": forecast["day"]["maxwind_mph"],
                        "humidity": forecast["day"]["avghumidity"]
                    })
            else:
                return Response({'error': 'Failed to retrieve weather data'}, status=response.status_code)

            # Set thời gian 1 ngày cho cache
            now = datetime.now()
            end_of_day = datetime.combine(now.date(), datetime.max.time())
            ttl = int((end_of_day - now).total_seconds())

            r.setex(cache_key, ttl, json.dumps(forecast_data))

        # Lấy dữ liệu current forecast
        current_forecast = forecast_data["forecasts"][0] if forecast_data["forecasts"] else None

        # Phân trang
        page = int(request.query_params.get('page', 1))  # Nhận tham số 'page'
        page_size = self.PAGE_SIZE

        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        # Cắt dữ liệu dựa trên phân trangs
        paginated_forecast = forecast_data["forecasts"][start_index:end_index]

        # Tổng số trang
        total_forecasts = len(forecast_data["forecasts"])
        total_pages = (total_forecasts + page_size - 1) // page_size

        return Response({
            "city": forecast_data["city"],
            "current_forecast": current_forecast,
            "forecasts": paginated_forecast,
            "total_page": total_pages,
        }, status=status.HTTP_200_OK)
