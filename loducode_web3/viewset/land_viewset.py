from django.utils.translation import ugettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from loducode_web3.models.land import Land
from loducode_web3.serializers.land_serializer import LandSerializer, LandCreateSerializer, LandListSerializer
from loducode_web3.utils import ActionBasedPermission

class LandViewSet(viewsets.ModelViewSet):  # pylint: disable=R0901 C0112
    queryset = Land.objects.all()
    serializer_class = LandSerializer
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
            return LandCreateSerializer
        if self.action == 'retrieve':
            return LandSerializer
        return LandListSerializer


EXAMPLE = (' ** { '
           '"name": "string", '
           '"description": "string", '
           '"image": "string", '
           '"attributes": "dict", '
           ' } **')

LandViewSet.__doc__ = """
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
    LIST=_("List of all Lands registered in the system."),
    CREATE=_("Create a Lands data.") + EXAMPLE,
    RETRIEVE=_("Returns the information of a specific Lands."),
    UPDATE=_("Update a Lands data.") + EXAMPLE,
    PARTIAL_UPDATE=_("Partially update a Lands data.") + ' ** { "description": "example name" } **',
    DESTROY=_("Destroy a Lands data."),
)
