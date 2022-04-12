from django.utils.translation import ugettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny


from loducode_web3.models.nft import Nft
from loducode_web3.serializers.nft_serializer import NftSerializer, NftListSerializer, NftCreateSerializer
from loducode_web3.utils import ActionBasedPermission


class NftViewSet(viewsets.ModelViewSet):  # pylint: disable=R0901 C0112
    queryset = Nft.objects.all()
    serializer_class = NftSerializer
    action_permissions = {
        IsAuthenticated: [],
        AllowAny: ['list', 'retrieve']
    }
    lookup_field = "cus_id"
    permission_classes = (ActionBasedPermission,)
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'id']
    ordering_fields = ['name']
    filter_fields = {

    }

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return NftCreateSerializer
        if self.action == 'retrieve':
            return NftSerializer
        return NftListSerializer


EXAMPLE = (' ** { '
           '"name": "string", '
           '"description": "string", '
           '"image": "string", '
           '"attributes": "dict", '
           ' } **')

NftViewSet.__doc__ = """
list:
   {LIST}
create:
    {CREATE}
retrieve:
   {RETRIEVE} 
update:
    {UPDATE}
partial_update:
    {PARTIAL_UPDATE}
destroy:
    {DESTROY}
""".format(
    LIST=_("List of all Nfts registered in the system."),
    CREATE=_("Create a Nfts data.") + EXAMPLE,
    RETRIEVE=_("Returns the information of a specific Nfts."),
    UPDATE=_("Update a Nfts data.") + EXAMPLE,
    PARTIAL_UPDATE=_("Partially update a Nfts data.") + ' ** { "description": "example name" } **',
    DESTROY=_("Destroy a Nfts data."),
)
