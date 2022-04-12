from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from loducode_utils.admin import AuditAdmin, AuditStackedInline

from loducode_web3.models.land import Land
from loducode_web3.models.attribute_land import AttributeLand


class AttributeInline(AuditStackedInline):
    model = AttributeLand
    extra = 0
    raw_id_fields = ('land',)


class LandResources(resources.ModelResource):
    class Meta:
        model = Land
        fields = ('id', 'name', 'description', 'attributes',)


@admin.register(Land)
class LandAdmin(AuditAdmin, ImportExportModelAdmin):
    resource_class = LandResources
    list_display = ('id', 'cus_id', 'name', 'image', 'attributes',)
    list_display_links = ('id', 'cus_id', 'name', 'image', 'attributes',)
    search_fields = ('name',)
    list_filter = ('id',)
    inlines = [AttributeInline]
