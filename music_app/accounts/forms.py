from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'age', 'gender', 'country')
        field_classes = {'username': auth_forms.UsernameField}


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
       # fields = ('username', 'first_name', 'last_name', 'email', 'age', 'country', 'gender')
        fields = ('username', 'email')

        field_classes = {
            'username': auth_forms.UsernameField,
        }