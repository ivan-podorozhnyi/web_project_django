from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.TextField()
    slug = models.SlugField(default="my-slug")
    content = models.TextField(null=True, blank=True)
