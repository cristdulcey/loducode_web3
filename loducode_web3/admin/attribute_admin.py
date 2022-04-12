from django.contrib import admin

from loducode_utils.admin import AuditAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from loducode_web3.models.attribute_land import AttributeLand


class AttributeLandResources(resources.ModelResource):
    class Meta:
        model = AttributeLand
        fields = ('id', 'name', 'value', 'land__name',)


@admin.register(AttributeLand)
class AttributeLAndAdmin(AuditAdmin, ImportExportModelAdmin):
    resource_class = AttributeLandResources
    list_display = ('id', 'name', 'value', 'land',)
    list_display_links = ('id', 'name', 'value', 'land',)
    raw_id_fields = ('land',)
    search_fields = ('name',)
    list_filter = ('id',)
