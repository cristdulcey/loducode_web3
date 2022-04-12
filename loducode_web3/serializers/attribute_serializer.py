from loducode_utils.serializers import AuditSerializer

from loducode_web3.models.attribute_land import AttributeLand
from loducode_web3.serializers.land_serializer import LandSerializer


class AttributeLandSerializer(AuditSerializer):
    nft = LandSerializer()

    class Meta:
        model = AttributeLand
        fields = ('id', 'name', 'value', 'land',)


class AttributeLandListSerializer(AuditSerializer):
    class Meta:
        model = AttributeLand
        fields = ('id', 'name', 'value', 'land',)


class AttributeLandCreateSerializer(AuditSerializer):
    class Meta:
        model = AttributeLand
        fields = ('id', 'name', 'value', 'land',)
