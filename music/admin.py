from django.contrib import admin
from .models import Song,Album,Playlist,Artist
# Register your models here.


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=['id','title','artist','album','audio_file']




@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display=['id','name','biography']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display=['id','title','artist','release_date','cover_image']


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display=['id','title','user','songs']