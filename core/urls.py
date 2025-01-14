from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

]
