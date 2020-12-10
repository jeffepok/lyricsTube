from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length = 200)
    lyrics = models.TextField(blank = True)

    def __str__(self):
        return self.title

class lyrics(models.Model):
    words = models.TextField(blank = True)