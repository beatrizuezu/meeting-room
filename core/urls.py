from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from core.api import urls as api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(api_urls))
]
