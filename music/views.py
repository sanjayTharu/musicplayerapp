from django.shortcuts import render,get_object_or_404,redirect
from .models import Song,Album,Artist,Playlist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password1')
        password2=request.POST.get('password2')

        print(name)
        print(email)
        print(password)
        print(password2)

        user=User.objects.filter(username=email)

        if user.exists():
            messages.info(request,'Email already Exists')
            return redirect('/register/')
        
        if password != password2:
            messages.info(request,'Password and confirm password didnot match')
            return redirect('/register/')
        else:
            user=User.objects.create_user(
                username=email
            )
            user.set_password(password)
            user.save()

            messages.info(request,'Account Created Successfully')

        return redirect('/login/')
    return render(request,'music/register.html')

def login_page(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)

        if not User.objects.filter(username=username,password=password).exists():
            messages.info(request,'Username doesnot exists')
            return redirect('/login/')
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/home/')
    return render(request, 'music/login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')


def index(request):
    songs=Song.objects.all()
    return render(request,'music/index.html',{'songs':songs})

def play_song(request,song_id):
    song= get_object_or_404(Song,pk=song_id)
    return render(request,'music/play_song.html',{'song':song})

def artist_detail(request,artist_id):
    artist=get_object_or_404(Artist,pk=artist_id)
    albums=Album.objects.filter(artist=artist)
    return render(request,'music/artist_detail.html',{'albums':albums})

def album_detail(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    songs=Song.objects.filter(album=album)
    return render(request,'music/album_detail.html',{'songs':songs})

def playlist_detail(request,playlist_id):
    playlist=get_object_or_404(Playlist,pk=playlist_id)
    songs=playlist.songs.all()
    return render(request,'music/playlist_detail.html',{'songs':songs})

def create_playlist(request):
    if request.method=='POST':
        playlist_title=request.POST['playlist_title']
        user=request.user
        playlist=Playlist.objects.create(title=playlist_title,user=user)
        return redirect('playlist_detail',playlist_id=playlist.id)
    else:
        return render(request,'music/create_playlist.html')
    
def add_song_to_playlist(request,playlist_id,song_id):
    playlist=get_object_or_404(Playlist,pk=playlist_id)
    song=get_object_or_404(Song,pk=song_id)
    playlist.songs.add(song)
    return redirect('playlist_detail',playlist_id=playlist.id)

def remove_song_from_playlist(request,playlist_id,song_id):
    playlist=get_object_or_404(Playlist,pk=playlist_id)
    song=get_object_or_404(Song,pk=song_id)
    playlist.songs.remove(song)
    return redirect('playlist_detail',playlist_id=playlist.id)


