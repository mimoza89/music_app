from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from music_app.albums.models import Album
from music_app.singers.models import Singer
from music_app.songs.models import Song
from music_app.songs.forms import SongCreateForm

# Create your views here.

@login_required
def add_a_song(request, pk):
    album = Album.objects.filter(pk=pk).get()
    singer = Singer.objects.filter(pk=album.released_by_id).get()
    if request.method == 'GET':
        form = SongCreateForm()
    else:
        form = SongCreateForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.in_the_album_id = album.pk
            song.released_by_id = singer.pk
            song.save()
            form.save_m2m()
            return redirect('album details', pk=album.pk)

    print(request.method)

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'songs/add.html', context)

def songs_in_an_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    singer = Singer.objects.filter(pk=album.released_by_id)
    songs = Song.objects.all()
    songs_in_the_album = songs.filter(in_the_album_id=pk).all()

    context = {
        'album': album,
        'songs_in_the_album': songs_in_the_album,
        'singer': singer,
    }

    return render(request, 'songs/songs-in-an-album.html', context)


