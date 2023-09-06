from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from colaboradores.api import viewsets as ColaboradoresViewSet

route = routers.DefaultRouter()
route.register(r'colaboradores/', ColaboradoresViewSet.ColaboradoresViewSet, basename="Colaboradores")

urlpatterns = [
    path('api/', include(route.urls)),
    path('', include('home.urls')),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
