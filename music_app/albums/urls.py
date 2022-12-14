from django.urls import path
from music_app.albums.views import all_albums, add_album, edit_album, delete_album, album_details

urlpatterns = (
    path('', all_albums, name='albums'),
    path('add/<int:pk>/', add_album, name='add album'),
    path('details/<int:pk>/', album_details, name='album details'),
    path('edit/<int:pk>/', edit_album, name='edit album'),
    path('delete/<int:pk>/', delete_album, name='delete album'),
)