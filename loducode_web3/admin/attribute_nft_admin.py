from django.contrib import admin

from loducode_utils.admin import AuditAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from loducode_web3.models.attribute_nft import AttributeNft


class AttributeNftResources(resources.ModelResource):
    class Meta:
        model = AttributeNft
        fields = ('id', 'name', 'value', 'nft__name',)


@admin.register(AttributeNft)
class AttributeNftAdmin(AuditAdmin, ImportExportModelAdmin):
    resource_class = AttributeNftResources
    list_display = ('id', 'name', 'value', 'nft',)
    list_display_links = ('id', 'name', 'value', 'nft',)
    raw_id_fields = ('nft',)
    search_fields = ('name',)
    list_filter = ('id', 'nft__cus_id')
