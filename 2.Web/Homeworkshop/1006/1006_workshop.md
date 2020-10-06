# 1006_workshop

### 1. Model & Admin

> 관리자 페이지를 활용하여 가수, 가수가 부른 노래 2개씩 작성한다.
>
> - Artist (필드: name)
> - Music (필드: artist와 1:N, title)

```python
# models.py
from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name}'


class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'
```

![image-20201006160356805](C:\Users\dltmd\Desktop\SSAFY\online-lecture\1006\1006_workshop.assets\image-20201006160356805.png)

![image-20201006160413220](C:\Users\dltmd\Desktop\SSAFY\online-lecture\1006\1006_workshop.assets\image-20201006160413220.png)

---

### 2. Serializer

> ArtistListSerializer
>
> - 모든 가수의 정보를 반환 (필드: id, title)
>
> ArtistSerializer
>
> - 상세 가수의 정보를 생성 및 반환 (필드: id, name, music_set, music_count)
>
> MusicListSerializer
>
> - 모든 음악의 정보를 반환 (필드: id, title)
>
> MusicSerializer
>
> - 상세 음악의 정보를 반환 (필드: id, title, artist)

```python
# serializers.py
from rest_framework import serializers
from .models import Artist, Music

class MusicListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Music
        fields= ['id', 'title']


class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ['id', 'title', 'artist']


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
```

---

### 3. url & views

> **GET & POST** api/v1/artists/
>
> - GET 요청 : 모든 가수의 id와 name 컬럼을 JSON으로 응답
> - POST 요청 : 가수의 정보 생성
>
> **GET**  api/v1/artists/<artist_pk>/
>
> - 특정 가수의 모든 컬럼을 JSON으로 응답
> - 특정 가수의 노래 정보와 노래의 개수 정보를 함께 응답
>
> **POST** api/v1/articles/<artist_pk>/music/
>
> - 특정 가수의 음악 정보 생성
>
> **GET** api/v1/music
>
> - 모든 음악의 id와 title 컬럼을 JSON으로 응답
>
> **GET & PUT & DELETE** api/v1/music/<music_pk>/
>
> - GET 요청 : 특정 음악의 모든 컬럼을 JSON으로 응답
> - PUT 요청 : 특정 음악의 정보를 수정
> - DELETE 요청 :특정 음악의 정보 삭제

```python
from django.shortcuts import render,get_object_or_404
from rest_framework import serializers

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Artist, Music
from .serializers import ArtistListSerializer, ArtistSerializer, MusicListSerializer, MusicSerializer

# Create your views here.
@api_view(['GET','POST'])
def artist_list_create(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(artists, many=True)
    else:
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)


@api_view(['POST'])
def music_create(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
    return Response(serializer.data)


@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicListSerializer(musics, many=True)
    return Response(serializer.data)
        

@api_view(['GET','PUT','DELETE'])
def music_detail_update_delete(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MusicSerializer(instance=music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    else:
        music.delete()
        return Response(
            {'message' : f'{music_pk}번 삭제!'},
            status=status.HTTP_204_NO_CONTENT
        )
```

![image-20201006161806189](C:\Users\dltmd\Desktop\SSAFY\online-lecture\1006\1006_workshop.assets\image-20201006161806189.png)

![image-20201006162320441](C:\Users\dltmd\Desktop\SSAFY\online-lecture\1006\1006_workshop.assets\image-20201006162320441.png)

![image-20201006163135556](C:\Users\dltmd\Desktop\SSAFY\online-lecture\1006\1006_workshop.assets\image-20201006163135556.png)

![image-20201006163242495](C:\Users\dltmd\Desktop\SSAFY\online-lecture\1006\1006_workshop.assets\image-20201006163242495.png)

![image-20201006164240812](C:\Users\dltmd\Desktop\SSAFY\online-lecture\1006\1006_workshop.assets\image-20201006164240812.png)

![image-20201006164414110](C:\Users\dltmd\Desktop\SSAFY\online-lecture\1006\1006_workshop.assets\image-20201006164414110.png)

![image-20201006164452191](C:\Users\dltmd\Desktop\SSAFY\online-lecture\1006\1006_workshop.assets\image-20201006164452191.png)