from django.utils.translation import ugettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from lands.models.attribute_land import AttributeLand
from lands.serializers.attribute_serializer import AttributeLandSerializer, AttributeLandListSerializer, \
    AttributeLandCreateSerializer
from loducode_web3.utils import ActionBasedPermission

class AttributeLandViewSet(viewsets.ModelViewSet):  # pylint: disable=R0901 C0112
    queryset = AttributeLand.objects.all()
    serializer_class = AttributeLandSerializer
    action_permissions = {
        IsAuthenticated: [],
        AllowAny: ['list', 'retrieve']
    }
    permission_classes = (ActionBasedPermission,)
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'id']
    ordering_fields = ['name']
    filter_fields = {
        'land': ['exact', ]
    }

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return AttributeLandCreateSerializer
        if self.action == 'retrieve':
            return AttributeLandSerializer
        return AttributeLandListSerializer


EXAMPLE = (' ** { '
           '"name": "string", '
           '"value": "string", '
           '"nft": "UUID", '
           ' } **')

AttributeLandViewSet.__doc__ = """
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
    LIST=_("List of all Attributes registered in the system."),
    CREATE=_("Create a Attributes data.") + EXAMPLE,
    RETRIEVE=_("Returns the information of a specific Attributes."),
    UPDATE=_("Update a Attributes data.") + EXAMPLE,
    PARTIAL_UPDATE=_("Partially update a Attributes data.") + ' ** { "name": "example name" } **',
    DESTROY=_("Destroy a Attributes data."),
)
