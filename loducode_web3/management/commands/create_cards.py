import random
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from loducode_web3.models.attribute_nft import AttributeNft
from loducode_web3.models.nft import Nft


class Command(BaseCommand):
    help = 'Create cards in data base'

    def handle(self, *args, **options):  # pylint: disable=R0914
        nfts_old = Nft.objects.all()
        nfts_old.delete()
        request = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php?type=Normal%20Monster')
        type_cards = ('Luchador', 'Tanque', 'Aquero', 'Mago')
        armies_cards = ('Puros', 'Impuros', 'Conocimiento', 'Libertarios', 'Fortuna', 'Alma', 'Luz')
        levels = ('Gold', 'Comun')
        rarity = ('Legendaria', 'Epica', 'Rara', 'Común')
        dict_prueba = {
            "2": "3",
            "3": "50",
            "4": "100",
            "5": "300"
        }
        if request.status_code == 200:
            count = 0
            try:
                res = request.json()
                for card in res['data']:
                    nft, created = Nft.objects.get_or_create(
                        name=card['name'][0:254],
                        description=card['desc'][0:554],
                        cost=0.0025,
                        date_publication=timezone.now().astimezone().date(),
                        cus_id=count + 1,
                        update_level=dict_prueba
                    )
                    if created:
                        image_content = ContentFile(requests.get(card['card_images'][0]['image_url']).content)
                        nft.image.save('{}.jpg'.format(card['name']), image_content)
                    attr_type = AttributeNft(
                        nft=nft,
                        value=type_cards[random.randint(0, 3)],
                        name='type'
                    )
                    attr_type.save()
                    attr_army = AttributeNft(
                        nft=nft,
                        value=armies_cards[random.randint(0, 6)],
                        name='army'
                    )
                    attr_army.save()
                    attr_rarity = AttributeNft(
                        nft=nft,
                        value=rarity[random.randint(0, 3)],
                        name='rareza'
                    )
                    attr_rarity.save()
                    attr_level = AttributeNft(
                        nft=nft,
                        value=levels[random.randint(0, 1)],
                        name='lamina'
                    )
                    attr_level.save()
                    attr_power = AttributeNft(
                        nft=nft,
                        value=int(random.randint(0, 10)),
                        name='power'
                    )
                    attr_power.save()
                    attr_mana = AttributeNft(
                        nft=nft,
                        value=int(random.randint(0, 10)),
                        name='mana'
                    )
                    attr_mana.save()
                    attr_def = AttributeNft(
                        nft=nft,
                        value=int(random.randint(0, 10)),
                        name='def'
                    )
                    attr_def.save()
                    attr_vel = AttributeNft(
                        nft=nft,
                        value=int(random.randint(0, 10)),
                        name='vel'
                    )
                    attr_vel.save()
                    attr_attribute = AttributeNft(
                        nft=nft,
                        value=card['attribute'],
                        name='attribute'
                    )
                    attr_attribute.save()
                    attr_life = AttributeNft(
                        nft=nft,
                        value=int(random.randint(0, 10)),
                        name='life'
                    )
                    attr_life.save()
                    self.stdout.write(self.style.SUCCESS('Successfully created {}'.format(card['name'])))
                    count += 1
            except Exception as err:
                raise CommandError(err)  # pylint: disable=W0707
            self.stdout.write(self.style.SUCCESS('Successfully created {} cards'.format(count)))
        else:
            raise CommandError('Url endpoint error')
