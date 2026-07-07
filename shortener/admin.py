from django.contrib import admin

from .models import Click, Link


class ClickInline(admin.TabularInline):
    model = Click
    extra = 0
    readonly_fields = ["ip_hashed", "referer", "created_at"]
    can_delete = False
    max_num = 20


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = [
        "short_code",
        "original_url",
        "clicks_count",
        "is_active",
        "created_at",
    ]
    list_filter = ["is_active", "created_at"]
    search_fields = ["short_code", "original_url"]
    inlines = [ClickInline]
    actions = ["deactivate_links"]

    def deactivate_links(self, request, queryset):
        queryset.update(is_active=False)

    deactivate_links.short_description = "Desactivar enlaces seleccionados"
