
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class BaseModelMixin(models.Model):
    slug = models.SlugField(_("In-app url"), editable=False)
    name = models.CharField(_("Name"), max_length=120)
    short_desc = models.CharField(_("Short description"), max_length=250)
    long_desc = models.CharField(_("Long description"), max_length=1024)

    date_created = models.DateTimeField(_("created on"), default=timezone.now)
    last_modified = models.DateTimeField(_("last modified"), auto_now=True)

    class Meta:
        abstract = True

    @property
    def short_description(self):
        return self.short_desc

    @property
    def long_description(self):
        return self.long_desc

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
