from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


class Meeting(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField()
    owner = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        "auth.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="owned_meetings",
    )

    class Meta:
        permissions = [
            ("can_view_meeting", "Can view meeting"),
            ("can_edit_meeting", "Can edit meeting"),
            ("can_delete_meeting", "Can delete meeting"),
        ]

    def __str__(self):
        return f"{self.title} ({self.date})"


class ActionItem(models.Model):
    meeting = models.ForeignKey(
        Meeting, on_delete=models.CASCADE, related_name="action_items"
    )
    description = models.CharField(max_length=300)
    owner = models.CharField(max_length=100)
    due_date = models.DateField()
    status = models.CharField(max_length=20, default="open")
    assigned_to = models.ForeignKey(
        "auth.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tasks",
    )

    class Meta:
        permissions = [
            ("can_view_action_item", "Can view action item"),
            ("can_complete_action_item", "Can complete action item"),
        ]

    def __str__(self):
        return f"{self.description} - {self.status}"
