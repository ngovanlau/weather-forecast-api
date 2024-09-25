# Weather Forecast API

Dự án này là một API dự báo thời tiết được xây dựng bằng Django và Django REST Framework. API cho phép người dùng truy cập dữ liệu dự báo thời tiết cho các thành phố khác nhau.

## Nội dung

- [Yêu cầu](#yêu-cầu)
- [Cài đặt](#cài-đặt)
  - [1. Build Bình Thường](#1-build-bình-thường)
  - [2. Build với Docker](#2-build-với-docker)
    - [A. Sử dụng Dockerfile](#a-sử-dụng-dockerfile)
    - [B. Sử dụng Docker Compose](#b-sử-dụng-docker-compose)
- [Truy cập API](#truy-cập-api)
- [Tài liệu thêm](#tài-liệu-thêm*)*

## Yêu cầu

- Python 3.8 trở lên
- Django 3.2 trở lên
- Django REST Framework
- Docker (nếu bạn muốn sử dụng Docker)
- Git

## Cài đặt

### 1. Build Bình Thường

Để build và chạy dự án bình thường mà không cần Docker, bạn cần làm theo các bước sau:

1. **Clone Repository:**

   ```bash
   git clone https://github.com/ngovanlau/weather-forecast-api.git
   cd weather-forecast-api
   ```

2. **Tạo và Kích Hoạt Môi Trường Ảo:**

   - Trên macOS/Linux:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - Trên Windows:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Cài Đặt Các Gói Cần Thiết:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Chạy Server:**

   ```bash
   python manage.py runserver
   ```

   Server sẽ chạy tại `http://127.0.0.1:8000/`.

### 2. Build với Docker

Bạn có thể build và chạy dự án bằng Docker bằng cách sử dụng Dockerfile hoặc Docker Compose.

#### A. Sử dụng Dockerfile

1. **Clone Repository:**

   ```bash
   git clone https://github.com/ngovanlau/weather-forecast-api.git
   cd weather-forecast-api
   ```

2. **Build Image Docker:**

   ```bash
   docker build -t weather-forecast-api .
   ```

3. **Chạy Container:**

   Trước khi chạy container, đảm bảo rằng bạn đã tạo tệp `.env` với các biến môi trường cần thiết.

   ```bash
   docker run -d -p 8000:8000 --env-file .env weather-forecast-api
   ```

   Sau khi chạy, bạn có thể truy cập API tại `http://localhost:8000`.

#### B. Sử dụng Docker Compose

1. **Clone Repository:**

   ```bash
   git clone https://github.com/ngovanlau/weather-forecast-api.git
   cd weather-forecast-api
   ```

2. **Chạy Dự Án bằng Docker Compose:**

   ```bash
   docker-compose up --build
   ```

   Docker Compose sẽ tự động build và chạy dự án. Sau khi hoàn tất, bạn có thể truy cập API tại `http://localhost:8000`.

## Truy cập API

Sau khi server đã chạy, bạn có thể truy cập API tại địa chỉ `http://localhost:8000`. Các endpoint chính bao gồm:

- **Dự báo thời tiết cho một thành phố:**

  ```
  GET /weathers/{city}/
  ```

  Trong đó `{city}` là tên của thành phố mà bạn muốn dự báo thời tiết.


## Tài liệu thêm

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)


**Ngô Văn Lâu**  
Email: ngovanlau2003@gmail.com