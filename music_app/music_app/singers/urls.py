from django.urls import path
from music_app.singers.views import add_singer, singer_details, all_singers, edit_singer_information, delete_singer

urlpatterns = (
   path('', all_singers, name='singers'),
   path('add/', add_singer, name='add singer'),
   path('details/<int:pk>/', singer_details, name='singer details'),
   path('edit/<int:pk>/', edit_singer_information, name='edit singer information'),
   path('delete/<int:pk>/', delete_singer, name='delete singer'),

)