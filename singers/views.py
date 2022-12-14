from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from music_app.albums.models import Album
from music_app.common.models import Comment
from music_app.singers.forms import SingerCreateForm, SingerEditForm, SingerDeleteForm
from music_app.singers.models import Singer

# Create your views here.


@login_required
def add_singer(request):
    if request.method == 'GET':
        form = SingerCreateForm()
    else:
        form = SingerCreateForm(request.POST)
        if form.is_valid():
            singer = form.save(commit=False)
            singer.owner = request.user
            singer.save()
            return redirect('profile details', pk=request.user.pk)

    context = {
        'form': form,
    }

    return render(request, 'singer/singer-add-page.html', context)


def singer_details(request, pk):
    singer = Singer.objects.filter(pk=pk).get()
    owner = request.user == singer.owner
    albums = Album.objects.filter(released_by=singer.pk).all()
    comments = Comment.objects.filter(singer_id=singer.pk).all()

    context = {
        'singer': singer,
        'owner': owner,
        'albums': albums,
        'comments': comments,
    }

    print(albums)

    return render(request, 'singer/singer-details-page.html', context)

def all_singers(request):
    singers = Singer.objects.all()
    context = {
        'singers': singers,
    }


    return render(request, 'singer/all-singers.html', context)

def edit_singer_information(request, pk):
    singer = Singer.objects.filter(pk=pk).get()
    is_owner = request.user == singer.owner
    if request.method == 'GET':
        form = SingerEditForm(instance=singer)
    else:
        form = SingerEditForm(request.POST, instance=singer)
        if form.is_valid():
            form.save()
            return redirect('singer details', pk=singer.pk)

    context = {
        'form': form,
        'singer': singer,
    }

    return render(request, 'singer/edit-singer-information.html', context)

def delete_singer(request, pk):
    singer = Singer.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = SingerDeleteForm(instance=singer)
    else:
        form = SingerDeleteForm(request.POST, instance=singer)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk=singer.owner_id)

    context = {
        'form': form,
        'singer': singer,
    }

    return render(request, 'singer/singer-delete-page.html', context)