
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from . models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name',
            'user_type', 'password1', 'password2',
        )
        widgets = {
            'user_type': forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'placeholder': 'Username',
            'class': 'input',
        })
        self.fields["email"].widget.attrs.update({
            'placeholder': 'Email',
            'class': 'input',
        })
        self.fields["first_name"].widget.attrs.update({
            'placeholder': 'First Name',
            'class': 'input',
        })
        self.fields["last_name"].widget.attrs.update({
            'placeholder': 'Last Name',
            'class': 'input',
        })
        self.fields["password1"].widget.attrs.update({
            'placeholder': 'Password',
            'class': 'input',
        })
        self.fields["password2"].widget.attrs.update({
            'placeholder': 'Confirm password',
            'class': 'input',
        })
        self.fields["user_type"].widget.attrs.update({
            'class': 'radio',
        })


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'user_type')


class UserAdminChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'user_type')
