from django.views import generic as views
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from music_app.albums.models import Album
from music_app.albums.forms import AlbumAddForm, AlbumEditForm
from music_app.singers.models import Singer
from music_app.songs.models import Song

# Create your views here.
UserModel = get_user_model()
def all_albums(request):
    albums = Album.objects.all()
    singers = Singer.objects.all()

    context = {
        'albums': albums,
        'singers': singers,
    }

    return render (request, 'albums/all-albums.html', context)

@login_required
def add_album(request, pk):
    singer = Singer.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = AlbumAddForm()
    else:
        form = AlbumAddForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.owner = request.user
            album.released_by_id = singer.pk
            album.save()
            form.save_m2m()
            return redirect('singer details', pk=singer.pk)

    context = {
        'form': form,
        'singer': singer,
    }
    return render(request, 'albums/add-album.html', context)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    owner = request.user == album.owner_id
    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album details', pk=album.pk)

    context = {
        'form': form,
        'owner': owner,
        'album': album,
    }

    return render(request, 'albums/edit-album.html', context)

def album_details(request, pk):
    album = Album.objects.filter(pk=pk).get()
    singer = Singer.objects.filter(pk=album.released_by_id).get()
    songs = Song.objects.filter(in_the_album_id=pk).all()


    context = {
        'album': album,
        'singer': singer,
        'songs': songs,
    }
    return render(request, 'albums/album-details.html', context)

def delete_album(request,pk):
    return render(request, 'albums/delete-album.html')