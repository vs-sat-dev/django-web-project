from django.db import models
from django.conf import settings


class Post(models.Model):
    published = (
        ('Draft', 'draft'),
        ('Published', 'published'),
    )

    image = models.ImageField(upload_to='blog_images')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, blank=False)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    status = models.CharField(max_length=32, choices=published, default='Draft')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
