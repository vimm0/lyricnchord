from django.contrib import admin
from django.urls import path, include
from rest_framework import serializers, viewsets, routers

from apps.core.models import Song, Artist


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('name')
    serializer_class = SongSerializer


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('name')
    serializer_class = ArtistSerializer


router = routers.DefaultRouter()
router.register(r'songs', SongViewSet)
router.register(r'artists', ArtistViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
