from django.urls import path, include

urlpatterns = [
    path("api/news", include("news.urls")),
]
