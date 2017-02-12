
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import newfolder
from newfolder.views import aboutView
from newsletter.views import HomeView, ContactView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView, name='HomeName'),
    url(r'^contact$', ContactView, name='contactName'),
    url(r'^about$', newfolder.views.aboutView, name='aboutName'),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)