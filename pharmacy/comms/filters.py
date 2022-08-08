from django.contrib.admin import SimpleListFilter
class PharmacyNames(SimpleListFilter):
    title = 'pharmacyname' # or use _('country') for translated title
    parameter_name = 'pharmacyname'

    def lookups(self, request, model_admin):
        pharmacynames = set([c.pharmacyname for c in model_admin.model.objects.all()])
        return ((i,i) for i in pharmacynames)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(pharmacyname__exact=self.value())
        else:
            return queryset
