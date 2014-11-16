from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    post_time = models.DateTimeField()

    def __unicode__(self):
        return self.title

