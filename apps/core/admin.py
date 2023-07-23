from django.contrib import admin

from apps.core.models import Artist, Band, Album, Song


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ['name', 'album_count']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_band_name', 'song_count']

    @admin.display(ordering='band__name', description='Band')
    def get_band_name(self, obj):
        return obj.band.name


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_album_name', 'get_band_name']

    @admin.display(description='Album')
    def get_album_name(self, obj):
        return obj.album.name

    @admin.display(description='Band')
    def get_band_name(self, obj):
        return obj.album.band.name
