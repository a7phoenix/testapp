from django.shortcuts import render
from rest_framework.generics import ListAPIView

from news.models import NewsModel
from news.api.serializers import NewsSerializer

class ApiNewsListView(ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer