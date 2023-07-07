from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _

from . models import Profile, User

from . forms import UserAdminCreationForm, UserAdminChangeForm


# admin.site.login = login_required(admin.site.login)
admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = UserAdminCreationForm
    form = UserAdminChangeForm


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
