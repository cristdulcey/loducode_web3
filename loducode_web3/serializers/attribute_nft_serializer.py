from loducode_utils.serializers import AuditSerializer

from loducode_web3.models.attribute_nft import AttributeNft
from loducode_web3.serializers.nft_serializer import NftSerializer


class AttributeNftSerializer(AuditSerializer):
    nft = NftSerializer()

    class Meta:
        model = AttributeNft
        fields = ('name', 'value', 'nft',)


class AttributeNftListSerializer(AuditSerializer):
    class Meta:
        model = AttributeNft
        fields = ('name', 'value', 'nft',)


class AttributeNftCreateSerializer(AuditSerializer):
    class Meta:
        model = AttributeNft
        fields = ('name', 'value', 'nft',)
