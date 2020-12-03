from rest_framework import serializers
from news.models import NewsModel

class TagsField(serializers.Field):

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data

class NewsSerializer(serializers.ModelSerializer):
    tags = TagsField(source="get_tags")
    class Meta:
        model = NewsModel
        fields = [
            'title_ru', 'title_uz',
            'body_ru', 'body_uz',
            'image',
            'date_published',
            'slug',
            'author',
            'tags',
        ]
