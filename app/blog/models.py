from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    post_image = models.FileField()
    publication_date = models.DateField()