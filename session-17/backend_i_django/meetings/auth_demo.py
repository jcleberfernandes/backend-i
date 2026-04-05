from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from meetings.models import Meeting, ActionItem


def demo_auth():
    print("=== Django Authentication Demo ===\n")

    print("1. Creating users...")
    admin_user, created = User.objects.get_or_create(
        username="admin", defaults={"is_staff": True, "is_superuser": True}
    )
    if created:
        admin_user.set_password("admin123")
        admin_user.save()
    print(f"   Admin user: {admin_user.username} (superuser={admin_user.is_superuser})")

    regular_user, created = User.objects.get_or_create(
        username="editor", defaults={"is_staff": True, "is_superuser": False}
    )
    if created:
        regular_user.set_password("editor123")
        regular_user.save()
    print(
        f"   Regular user: {regular_user.username} (superuser={regular_user.is_superuser})"
    )

    print("\n2. Creating groups...")
    viewers_group, _ = Group.objects.get_or_create(name="Viewers")
    editors_group, _ = Group.objects.get_or_create(name="Editors")
    print(f"   Created groups: Viewers, Editors")

    print("\n3. Getting content types...")
    meeting_ct = ContentType.objects.get_for_model(Meeting)
    action_ct = ContentType.objects.get_for_model(ActionItem)
    print(f"   Meeting content type: {meeting_ct}")
    print(f"   ActionItem content type: {action_ct}")

    print("\n4. Getting custom permissions...")
    can_view_meeting = Permission.objects.get(
        codename="can_view_meeting", content_type=meeting_ct
    )
    can_edit_meeting = Permission.objects.get(
        codename="can_edit_meeting", content_type=meeting_ct
    )
    print(f"   can_view_meeting: {can_view_meeting}")
    print(f"   can_edit_meeting: {can_edit_meeting}")

    print("\n5. Assigning permissions to groups...")
    editors_group.permissions.add(can_view_meeting, can_edit_meeting)
    regular_user.groups.add(editors_group)
    print(f"   Added permissions to Editors group")
    print(f"   Added regular_user to Editors group")

    print("\n6. Checking user permissions...")
    print(f"   admin_user has perms: {admin_user.get_all_permissions()}")
    print(f"   regular_user has perms: {regular_user.get_all_permissions()}")
    print(
        f"   regular_user in Editors: {regular_user.groups.filter(name='Editors').exists()}"
    )

    print("\n7. Testing permission checks...")
    print(
        f"   regular_user.can_view_meeting: {regular_user.has_perm('meetings.can_view_meeting')}"
    )
    print(
        f"   regular_user.can_edit_meeting: {regular_user.has_perm('meetings.can_edit_meeting')}"
    )
    print(
        f"   regular_user.can_delete_meeting: {regular_user.has_perm('meetings.can_delete_meeting')}"
    )

    print("\n=== Demo Complete ===")
    print("\nTo run this demo:")
    print("  python manage.py shell")
    print("  >>> from meetings.auth_demo import demo_auth")
    print("  >>> demo_auth()")


if __name__ == "__main__":
    demo_auth()
