from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.db.models import Q
from .models import Meeting, ActionItem


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date", "owner", "created_by")
    list_filter = ("date", "owner")
    search_fields = ("title", "owner")
    readonly_fields = ("created_by",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(Q(created_by=request.user) | Q(created_by__isnull=True))


@admin.register(ActionItem)
class ActionItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "meeting",
        "description",
        "owner",
        "due_date",
        "status",
        "assigned_to",
    )
    list_filter = ("status", "owner")
    search_fields = ("description", "owner")


admin.site.unregister(Group)
