from django.urls import path

from music_app.common.views import index, make_a_comment, all_comments_for_the_singer

urlpatterns = (
    path('', index, name='index'),
    path('comment/<int:singer_id>/', make_a_comment, name='make a comment'),
    path('comments/<int:pk>/', all_comments_for_the_singer, name='comments for the singer')
)