from loducode_utils.serializers import AuditSerializer

from loducode_web3.models.nft import Nft


class NftSerializer(AuditSerializer):
    class Meta:
        model = Nft
        fields = ('cus_id', 'name', 'description', 'image', 'attributes')


class NftListSerializer(AuditSerializer):
    class Meta:
        model = Nft
        fields = ('cus_id', 'name', 'description', 'image', 'attributes')


class NftCreateSerializer(AuditSerializer):
    class Meta:
        model = Nft
        fields = ('cus_id', 'name', 'description', 'image', 'attributes')
