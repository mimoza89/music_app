from django.urls import path

from music_app.accounts.views import SignInView, SignUpView, SignOutView, ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = (
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('profile/details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='edit profile'),
    path('profile/delete/<int:pk>/', ProfileDeleteView.as_view(), name='delete profile'),
)