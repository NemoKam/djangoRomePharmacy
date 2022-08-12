from django.contrib import admin
from .models import Comment
from .filters import PharmacyNames
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author','pharmacyname')
    list_filter = (PharmacyNames,)
    search_fields = ['text']
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        return queryset, use_distinct
admin.site.register(Comment, CommentAdmin)