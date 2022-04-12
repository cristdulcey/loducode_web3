from typing import Optional

from django.db import models
from django.utils.translation import gettext as _

from loducode_utils.models.audit import Audit

from loducode_web3.managers.attribute_nft_manager import AttributeNftManager


class AttributeNft(Audit):
    model_name = 'AttributesNft'

    nft: Optional = models.ForeignKey(to='loducode_web3.nft', verbose_name=_('Nft'), on_delete=models.CASCADE, blank=True,
                                      null=True)
    name: str = models.CharField(_('Name'), max_length=255)
    value: str = models.CharField(_('Value'), max_length=555, blank=True, null=True)

    objects = AttributeNftManager()

    class Meta:
        verbose_name = _('Attribute Nft')
        verbose_name_plural = _('Attributes Nft')

    def __str__(self):
        return f'{self.name}'

