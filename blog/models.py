from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=15)
    slug=models.CharField(max_length=200)
    timeStamp=models.DateTimeField(blank=True)
    content=HTMLField()

    def __str__(self):
        return self.title + " by " + self.author
