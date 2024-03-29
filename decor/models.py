from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)


class Topic(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    categories = models.ManyToManyField(Category, related_name='topics')


