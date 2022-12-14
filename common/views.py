from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from music_app.common.forms import CommentForm
from music_app.common.models import Comment
from music_app.singers.models import Singer


# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def make_a_comment(request, id):
    singer = Singer.objects.filter(id=id).get()
    form = CommentForm(request.POST)
    print(form.is_valid())
    print(f'Method used: {request.method}')

    if form.is_valid():
        form.save()
#        comment.singer_id = singer.pk
 #       comment.owner_id = request.user
  #      comment.save()
        return redirect('index')
    else:
        return redirect('singers')

    #    print(request.method)


def all_comments_for_the_singer(request, pk):
    singer = Singer.objects.filter(pk=pk).get()
    comments = Comment.objects.filter(singer_id=pk)

    context = {
        'singer': singer,
        'comments': comments,
    }

    print(comments.count)

    return render(request, 'common/all-comments-for-the-singer.html', context)
