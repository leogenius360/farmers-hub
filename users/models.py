
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    USER_TYPE = (
        ('farmer', _("FARMER")),
        ('store_keeper', _("STORE KEEPER")),
        ('support', _("SUPPORT")),
    )

    user_type = models.CharField(
        _("Choice"), max_length=60, choices=USER_TYPE,
        help_text=_("Your Profession ...!"), default=USER_TYPE[0]
    )

    REQUIRED_FIELDS = ['user_type',]


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='user_profile', on_delete=models.CASCADE,
    )
    first_name = models.CharField(
        _("First name"), max_length=150, blank=True
    )
    last_name = models.CharField(
        _("Last name"), max_length=150, blank=True
    )
    bio = models.TextField(_("Bio"), null=True, blank=True)

    # phone_number = PhoneNumberField(
    #     max_length=18, unique=True, null=True, blank=True,
    #     help_text=_("Enter your contact (phone) number ...!"),
    # )

    date_created = models.DateTimeField(_("Date created"), auto_now=True,)
    last_edited = models.DateTimeField(_("Last Edited"), auto_now=True,)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})
