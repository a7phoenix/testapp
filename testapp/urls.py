from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),

    # REST_FRAMEWORK
    path('api/news/', include('news.api.urls', 'news_api')),
    path('i18n/', include('django.conf.urls.i18n')),

]

urlpatterns += i18n_patterns(

    path('api/news/', include('news.api.urls')),

)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)