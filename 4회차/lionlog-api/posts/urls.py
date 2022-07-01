from django.contrib import admin
from django.urls import path, include 

from rest_framework import routers
from posts.views import PostModelViewSet 

router = routers.DefaultRouter()
router.register(r'posts', PostModelViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]
