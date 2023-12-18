from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from posts.sitemaps import *

urlpatterns = [
    path('9&c78WCLRYeDAldsyIOl1yeiL9XP/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('posts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'posts.views.page_not_found_view'
