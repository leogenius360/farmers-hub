from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from utils import get_anonymous_user

from . mixins import FarmModelMixin


UserModel = settings.AUTH_USER_MODEL


class FarmManagement(FarmModelMixin):
    created_by = models.ForeignKey(
        UserModel, on_delete=models.SET_DEFAULT, default=get_anonymous_user,
        related_name='user_created_farm_mgt', verbose_name=_("Created by"))

    long_desc = models.TextField(_("Long description"),)

    class Meta:
        verbose_name = _("Farm management")
        verbose_name_plural = _("Farm managements")

    def get_absolute_url(self):
        return reverse("farm_mgt_detail", kwargs={"slug": self.slug})


class ProductManagement(FarmModelMixin):
    created_by = models.ForeignKey(
        UserModel, on_delete=models.SET_DEFAULT, default=get_anonymous_user,
        related_name='user_created_product_mgt', verbose_name=_("Created by"))

    long_desc = models.TextField(_("Long description"),)

    class Meta:
        verbose_name = _("Product management")
        verbose_name_plural = _("Product managements")

    def get_absolute_url(self):
        return reverse("product_mgt_detail", kwargs={"slug": self.slug})


class Farm(FarmModelMixin):
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE,
        related_name='user_farms', verbose_name=_("Farm owner"))

    custom_mgt = models.ManyToManyField(
        FarmManagement, related_name='farm_custom_mgt',
        verbose_name=_("Custom managements/plans"))

    adapted_mgt = models.ManyToManyField(
        FarmManagement, related_name='farm_adapted_mgt',
        verbose_name=_("Adapted managements/plans"))

    class Meta:
        verbose_name = _("Farm")
        verbose_name_plural = _("Farms")

    def get_absolute_url(self):
        return reverse("farm_product_detail", kwargs={"slug": self.slug})


class FarmProduct(FarmModelMixin):
    farm = models.ForeignKey(
        Farm, on_delete=models.CASCADE, related_name='farm_products',
        verbose_name=_("Farm"),)

    custom_mgt = models.ManyToManyField(
        FarmManagement, related_name='product_custom_mgt',
        verbose_name=_("Custom managements/plans"))

    adapted_mgt = models.ManyToManyField(
        FarmManagement, related_name='product_adapted_mgt',
        verbose_name=_("Adapted managements/plans"))

    class Meta:
        verbose_name = _("Farm product")
        verbose_name_plural = _("Farm products")

    def get_absolute_url(self):
        return reverse("farm_product_detail", kwargs={"slug": self.slug})



