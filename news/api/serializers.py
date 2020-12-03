from rest_framework import serializers
from news.models import NewsModel, TaggableManager


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = [
            'title_ru', 'title_uz',
            'body_ru', 'body_uz',
            'image',
            'date_published',
            'slug',
            'author',
            # 'tags',
        ]