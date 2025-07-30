from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    # path('', include('main.urls'), name='main'),  # all patters must be at __init__.py file, or just use include('main.urls')
]

urlpatterns += i18n_patterns(  # adding localization, will be translated all main app
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name='main')
)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )