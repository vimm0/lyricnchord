from django.contrib import admin
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Band(models.Model):
    name = models.CharField(max_length=255)
    artists = models.ManyToManyField(Artist)
    genre = models.ManyToManyField(Genre, blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    @admin.display(description='Albums')
    def album_count(self):
        return self.album_set.count()


class Album(models.Model):
    name = models.CharField(max_length=255)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @admin.display(description='Songs')
    def song_count(self):
        return self.song_set.count()


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    lyrics = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
