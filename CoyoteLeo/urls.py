from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
