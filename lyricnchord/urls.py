from django.contrib import admin
from django.urls import path, include
from rest_framework import serializers, viewsets, routers

from apps.core.models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


router = routers.DefaultRouter()
router.register(r'songs', SongViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
