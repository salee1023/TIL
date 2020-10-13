from rest_framework import serializers
from .models import Artist, Music

class MusicListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Music
        fields= ['id', 'title']


class MusicSerializer(serializers.ModelSerializer):

    artist_name = serializers.CharField(
        source='artist.name'
    )

    class Meta:
        model = Music
        fields = ['id', 'title', 'artist', 'artist_name']


class ArtistListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artist
        fields = ['id', 'name']


class ArtistSerializer(serializers.ModelSerializer):
    
    music_set = MusicSerializer(
        many=True, read_only=True
    )

    music_count = serializers.IntegerField(
        source='music_set.count', read_only=True
    )

    class Meta:
        model = Artist
        fields = ['id', 'name', 'music_set', 'music_count']

