from django.urls import path
from news.api.views import ApiNewsListView

app_name = 'news'

urlpatterns = [
    path('news/', ApiNewsListView.as_view(), name="news_list"),
]
