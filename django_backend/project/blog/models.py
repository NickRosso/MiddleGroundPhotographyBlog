from django.db import models
from django.contrib.auth.models import User
from exiffield.fields import ExifField
from exiffield.getters import exifgetter

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class ImageAlbum(models.Model):
    name = models.CharField(max_length=500, default="")
    images = models.ManyToManyField('Image', default="", blank=True)
    def default(self):
        return self.images.filter(default=True).first()

class Image(models.Model):
    name = models.CharField(max_length=500)
    source = models.ImageField(upload_to='blog_post_images/')
    camera = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    lensModel = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    filetype = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    software = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    artist = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    exposure = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    shutterSpeed = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    fstop = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    focalLength = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    aperture = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    colorSpace = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    exposureCompensation = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    flash = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    meteringMode = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    cameraMode = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    ISO = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    originalDate = models.CharField(
        editable=False,
        blank=True,
        default="",
        max_length=500,
    )
    exif = ExifField(source='source', denormalized_fields={
        'camera': exifgetter('Model'),
        'lensModel': exifgetter('LensModel'),
        'filetype': exifgetter('FileType'),
        'software': exifgetter('Software'),
        'artist': exifgetter('Artist'),
        'exposure': exifgetter('ExposureTime'),
        'shutterSpeed': exifgetter('ShutterSpeedValue'),
        'fstop': exifgetter('FNumber'),
        'focalLength': exifgetter('focalLength'),
        'aperture': exifgetter('ApertureValue'),
        'colorSpace': exifgetter('ColorSpace'),
        'exposureCompensation': exifgetter('ExposureCompensation'),
        'flash': exifgetter('Flash'),
        'meteringMode': exifgetter('MeteringMode'),
        'cameraMode': exifgetter('ExposureProgram'),
        'ISO': exifgetter('ISO'),
        'originalDate': exifgetter('DateTimeOriginal')}
        )

class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') 
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    album = models.ForeignKey(ImageAlbum, related_name='post_album', on_delete=models.CASCADE, default="", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title