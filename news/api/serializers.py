from rest_framework import serializers
from news.models import NewsModel

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = [
            'title',
            'body',
            'image',
            'date_published',
            'slug',
            'author',
            'tags',
        ]