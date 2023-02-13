
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from teacher import urls as teacherUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('api/', include(teacherUrls)),
]
