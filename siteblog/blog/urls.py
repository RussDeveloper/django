from django.contrib import admin
from django.urls import path
from .views import *

from django.conf.urls.static import static
from siteblog import settings

urlpatterns = [
    path('', index, name='home'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
