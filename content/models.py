from django.db import models

class Genre(models.Model):

    name = models.CharField(max_length=255, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Song(models.Model):

    title = models.CharField(max_length=255, null=False)
    cover_art = models.ImageField(default="cover_art.png")
    audio = models.FileField(null=False)
    artist = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey(Genre, default=1, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Catalogue(models.Model):

    title =  models.CharField(max_length=255, null=False)
    cover_art = models.ImageField(default="cover_art.png")
    songs = models.ManyToManyField(Song)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    