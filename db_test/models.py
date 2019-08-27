from django.db import models
from django.utils import timezone


class User(models.Model):
   first_name = models.CharField(max_length=255)
   last_name = models.CharField(max_length=255)

   def __str__(self):
      return self.first_name


class Blog(models.Model):
   title = models.CharField(max_length=255)
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   created = models.DateTimeField(default=timezone.now())
   subscribers = models.ManyToManyField(User, related_name='subscriptions')

   def __str__(self):
      return self.title


class Topic(models.Model):
   title = models.CharField(max_length=255)
   blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   created = models.DateTimeField(default=timezone.now())
   likes = models.ManyToManyField(User, related_name='likes')

   def __str__(self):
      return self.title
