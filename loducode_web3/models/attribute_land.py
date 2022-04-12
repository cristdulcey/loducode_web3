from typing import Optional

from django.db import models
from django.utils.translation import gettext as _

from loducode_utils.models.audit import Audit

from loducode_web3.managers.attribute_lands_manager import AttributeLandManager


class AttributeLand(Audit):
    model_name = 'AttributeLand'

    land: Optional = models.ForeignKey(to='loducode_web3.land', verbose_name=_('Land'), on_delete=models.CASCADE, blank=True,
                                       null=True)
    name: str = models.CharField(_('Name'), max_length=255)
    value: str = models.CharField(_('Value'), max_length=555, blank=True, null=True)

    objects = AttributeLandManager()

    class Meta:
        verbose_name = _('Attribute Land')
        verbose_name_plural = _('Attributes Lands')

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def autocomplete_search_fields():
        return 'name'
