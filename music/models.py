from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Artist(models.Model):
    name=models.CharField(max_length=150)
    biography=models.TextField()

    def __str__(self):
        return self.name
    

class Album(models.Model):
    title=models.CharField(max_length=150)
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    release_date=models.DateField()
    cover_image=models.ImageField(upload_to='album_covers/')

    def __str__(self):
        return self.title


class Song(models.Model):
    title=models.CharField(max_length=150)
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    audio_file=models.FileField(upload_to='audio/')


    def __str__(self):
        return self.title
    

class Playlist(models.Model):
    title=models.CharField(max_length=150)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    songs=models.ForeignKey(Song,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


