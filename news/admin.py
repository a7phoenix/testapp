from django.contrib import admin
from django import forms

from news.models import NewsModel
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# @admin.register(NewsModel)
# class UngNewsModelAdmin(TranslationAdmin):
#     news_body_ru = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())
#     news_body_uz = forms.CharField(label='Tekst', widget=CKEditorUploadingWidget())
#
#     class Meta:
#         model = NewsModel
#         fields = '__all__'

class NewsAdmin(TranslationAdmin):
    pass

admin.site.register(NewsModel, NewsAdmin)