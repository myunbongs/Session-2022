from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.serializers import PostModelSerializer

class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)

