from django.contrib import admin
from .models import Post, Image, ImageAlbum

# Register your models here.
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(ImageAlbum)