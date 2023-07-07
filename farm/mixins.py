
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from utils.model_mixins import BaseModelMixin


class FarmModelMixin(BaseModelMixin):

    class Meta:
        abstract = True

    @property
    def adapted_managements(self):
        return self.adapted_mgt.all()

    @property
    def custom_managements(self):
        return self.custom_mgt.all()
