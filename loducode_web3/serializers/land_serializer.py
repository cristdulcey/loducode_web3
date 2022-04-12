from loducode_utils.serializers import AuditSerializer

from loducode_web3.models.land import Land


class LandSerializer(AuditSerializer):
    class Meta:
        model = Land
        fields = ('cus_id', 'name', 'description', 'image', 'attributes',)


class LandListSerializer(AuditSerializer):
    class Meta:
        model = Land
        fields = ('cus_id', 'name', 'description', 'image', 'attributes',)


class LandCreateSerializer(AuditSerializer):
    class Meta:
        model = Land
        fields = ('cus_id', 'name', 'description', 'image', 'attributes',)
