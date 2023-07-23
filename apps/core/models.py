from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Band(models.Model):
    name = models.CharField(max_length=255)
    artists = models.ManyToManyField(Artist)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
