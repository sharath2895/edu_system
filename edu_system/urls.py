
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from student import urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('api/v1/student/', include(urls)),

]
