from django.contrib.auth import views as auth_views, get_user_model, login
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render

from music_app.accounts.forms import UserCreateForm, UserEditForm
from music_app.singers.models import Singer

# Create your views here.

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        login(request, self.object)
        return response


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class ProfileDetailsView(views.DetailView):
    template_name = 'accounts/profile-details.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = self.request.user == self.object
        context['singers'] = Singer.objects.all()
        context['singers_count'] = self.object.singer_set.count()
        print(context['singers_count'])
        print()

        return context

class ProfileEditView(views.UpdateView):
    template_name = 'accounts/profile-edit.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'age', 'gender', 'country')
    #form_class = UserEditForm

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={
            'pk': self.request.user.pk,
        })

class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/delete-profile.html'
    model = UserModel
    success_url = reverse_lazy('index')
