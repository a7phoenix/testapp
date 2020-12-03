from modeltranslation.translator import register, TranslationOptions
from news.models import NewsModel

@register(NewsModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')