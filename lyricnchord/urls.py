from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import serializers, viewsets, routers

from apps.core.models import Song, Artist, Band


class SongSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    albums = serializers.SerializerMethodField()
    artist = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ('id', 'name', 'albums', 'image', 'lyrics', 'artist')
    
    def get_image(self, song):
        request = self.context.get('request')
        photo_url = song.album.first().cover.url if song.album else None
        return request.build_absolute_uri(photo_url)
    
    def get_albums(self, song):
        albums = [{'id': album.id, 'name': album.name} for album in song.album.all()]
        return albums
    
    def get_artist(self, song):
        artist = song.album.first().band if song.album else None
        return {
            'id': artist.id,
            'name': artist.name
        }


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('name')
    serializer_class = SongSerializer


class BandSerializer(serializers.ModelSerializer):
    artists = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()
    songs = serializers.SerializerMethodField()

    class Meta:
        model = Band
        fields = ('id', 'name', 'artists', 'genres', 'bio', 'image', 'songs')
    
    def get_artists(self, band):
        artists = [{'id': artist.id, 'name': artist.name} for artist in band.artist.all()]
        return artists

    def get_genres(self, band):
        genres = [{'id': genre.id, 'name': genre.name} for genre in band.genre.all()]
        return genres

    def get_songs(self, band):
        album_ids = band.album_set.values_list('id', flat=True)
        songs = Song.objects.filter(album__in=album_ids)
        songs = [{'id': song.id, 'name': song.name} for song in songs]
        return songs


class BandViewSet(viewsets.ModelViewSet):
    queryset = Band.objects.all().order_by('name')
    serializer_class = BandSerializer


router = routers.DefaultRouter()
router.register(r'songs', SongViewSet)
router.register(r'artists', BandViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #new
