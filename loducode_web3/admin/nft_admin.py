from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from loducode_utils.admin import AuditStackedInline, AuditAdmin

from loducode_web3.models.nft import Nft
from loducode_web3.models.attribute_nft import AttributeNft


class AttributeInline(AuditStackedInline):
    model = AttributeNft
    extra = 0
    raw_id_fields = ('nft',)


class NftResources(resources.ModelResource):
    class Meta:
        model = Nft
        fields = ('id', 'name', 'description', 'attributes',)


@admin.register(Nft)
class NftAdmin(AuditAdmin, ImportExportModelAdmin):
    resource_class = NftResources
    list_display = ('id', 'name', 'image', 'attributes',)
    list_display_links = ('id', 'name', 'image', 'attributes',)
    search_fields = ('name',)
    list_filter = ('cus_id',)
    inlines = [AttributeInline]
    ordering = ('cus_id',)
