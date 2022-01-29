from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, ImageAlbum, Image

class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ('exif',)

class ImageAlbumSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = ImageAlbum
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    author = PostUserSerializer(many=False, read_only=True)
    album = ImageAlbumSerializer(many=False, read_only=True)
    class Meta:
        model = Post
        fields = '__all__'