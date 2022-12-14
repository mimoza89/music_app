from django.urls import path
from music_app.songs.views import songs_in_an_album, add_a_song

urlpatterns = (
    path('add/<int:pk>', add_a_song, name='add a song'),
    path('<int:pk>/', songs_in_an_album, name='songs in the album'),
)