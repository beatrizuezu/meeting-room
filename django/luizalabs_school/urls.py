from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from luizalabs_school.meetings import urls as meetings_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(meetings_url))
]
