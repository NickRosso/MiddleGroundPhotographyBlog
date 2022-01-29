from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, ImageSerializer
from .models import Post, Image

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
