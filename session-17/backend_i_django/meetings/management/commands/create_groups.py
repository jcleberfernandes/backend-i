from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from meetings.models import Meeting, ActionItem


class Command(BaseCommand):
    help = "Create groups and assign permissions for meetings app"

    def handle(self, *args, **options):
        self.stdout.write("Creating groups and permissions...\n")

        meeting_content_type = ContentType.objects.get_for_model(Meeting)
        action_content_type = ContentType.objects.get_for_model(ActionItem)

        viewers_group, _ = Group.objects.get_or_create(name="Viewers")
        editors_group, _ = Group.objects.get_or_create(name="Editors")
        admins_group, _ = Group.objects.get_or_create(name="Admins")

        viewer_perms = [
            Permission.objects.get(
                codename="can_view_meeting", content_type=meeting_content_type
            ),
            Permission.objects.get(
                codename="can_view_action_item", content_type=action_content_type
            ),
        ]
        viewers_group.permissions.set(viewer_perms)

        editor_perms = [
            Permission.objects.get(
                codename="can_view_meeting", content_type=meeting_content_type
            ),
            Permission.objects.get(
                codename="can_edit_meeting", content_type=meeting_content_type
            ),
            Permission.objects.get(
                codename="can_view_action_item", content_type=action_content_type
            ),
            Permission.objects.get(
                codename="can_complete_action_item", content_type=action_content_type
            ),
        ]
        editors_group.permissions.set(editor_perms)

        all_meeting_perms = Permission.objects.filter(content_type=meeting_content_type)
        all_action_perms = Permission.objects.filter(content_type=action_content_type)
        admins_group.permissions.set(list(all_meeting_perms) + list(all_action_perms))

        self.stdout.write(self.style.SUCCESS("Groups created successfully!"))
        self.stdout.write(f"  - Viewers: {[p.codename for p in viewer_perms]}")
        self.stdout.write(f"  - Editors: {[p.codename for p in editor_perms]}")
        self.stdout.write(f"  - Admins: All permissions")
