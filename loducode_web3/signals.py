from django.db.models.signals import post_save
from django.dispatch import receiver

from loducode_web3.models.attribute_nft import AttributeNft
from loducode_web3.models.attribute_land import AttributeLand


@receiver(post_save, sender=AttributeNft, weak=False)
def update_attributes_nft(
        sender, instance, raw, created, using, update_fields, weak=False,
        **kwargs  # pylint: disable=R0913 W0613
):
    attributes_nft = AttributeNft.objects.filter(nft__id=instance.nft.id)
    aux = []
    for attribute in attributes_nft:
        aux.append({
            "trait_type": attribute.name,
            "value": attribute.value,
        })
    instance.nft.attributes = aux
    instance.nft.save()


@receiver(post_save, sender=AttributeLand, weak=False)
def update_attributes_land(
        sender, instance, raw, using, update_fields, weak=False,
        **kwargs  # pylint: disable=R0913 W0613
):
    attributes_land = AttributeLand.objects.filter(land__id=instance.land.id)
    aux = []
    for attribute in attributes_land:
        aux.append({
            "trait_type": attribute.name,
            "value": attribute.value,
        })
    instance.land.attributes = aux
    instance.land.save()
