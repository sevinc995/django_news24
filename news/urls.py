from django.urls import path
from .views import NewsCoreList

urlpatterns = [
    path('', NewsCoreList.as_view(), name='news-list'),
]