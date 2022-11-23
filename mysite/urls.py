from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mysite import settings
from selfedu.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('step0', include('step0.urls')),
    path('', include('selfedu.urls')),

]

handler404 = pageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
