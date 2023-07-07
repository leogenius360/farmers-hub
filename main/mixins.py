
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from utils.model_mixins import BaseModelMixin


class MarketModelMixin(BaseModelMixin):

    long_desc = models.TextField(_("Long description"),)
    img = models.ImageField(
        _("Image"), upload_to='market/product_imgs', height_field=None, width_field=None)

    date_created = models.DateTimeField(_("created on"), default=timezone.now)
    last_modified = models.DateTimeField(_("last modified"), auto_now=True)

    class Meta:
        abstract = True
