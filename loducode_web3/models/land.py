import os
from datetime import date

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.translation import gettext as _
from loducode_utils.models import Audit

from loducode_web3.managers.land_manager import LandManager


def create_path_land(instance, filename):
    return os.path.join(
        instance.name,
        filename
    )


class Land(Audit):
    model_name = 'Land'

    cus_id: int = models.BigIntegerField(verbose_name=_('Cus id'), default=12, unique=True)
    name: str = models.CharField(_('Name'), max_length=255)
    description: str = models.CharField(_('Description'), max_length=555, blank=True, null=True)
    image: str = models.FileField(
        verbose_name=_('Image'), upload_to=create_path_land, blank=True, null=True
    )
    attributes: dict = JSONField(verbose_name=_('Attributes'), null=True, blank=True, default=dict)
    cost: float = models.FloatField(verbose_name='Cost', default=0.0)
    date_publication: date = models.DateField()
    date_created: date = models.DateField(auto_now=True)

    objects = LandManager()

    class Meta:
        verbose_name = _('Land')
        verbose_name_plural = _('Lands')

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def autocomplete_search_fields():
        return 'name'
