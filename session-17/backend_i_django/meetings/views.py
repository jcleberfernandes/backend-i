from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Meeting, ActionItem


@login_required
def meeting_list(request):
    meetings = Meeting.objects.all()
    return render(request, "meetings/meeting_list.html", {"meetings": meetings})


@login_required
@permission_required("meetings.can_view_meeting", raise_exception=True)
def meeting_detail(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    return render(request, "meetings/meeting_detail.html", {"meeting": meeting})


class MeetingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Meeting
    fields = ["title", "date", "owner"]
    template_name = "meetings/meeting_form.html"
    success_url = reverse_lazy("meeting_list")
    permission_required = "meetings.can_edit_meeting"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class MeetingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Meeting
    fields = ["title", "date", "owner"]
    template_name = "meetings/meeting_form.html"
    success_url = reverse_lazy("meeting_list")
    permission_required = "meetings.can_edit_meeting"


class MeetingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Meeting
    template_name = "meetings/meeting_confirm_delete.html"
    success_url = reverse_lazy("meeting_list")
    permission_required = "meetings.can_delete_meeting"


@login_required
@permission_required("meetings.can_view_action_item", raise_exception=True)
def action_item_detail(request, pk):
    action_item = get_object_or_404(ActionItem, pk=pk)
    return render(
        request, "meetings/actionitem_detail.html", {"action_item": action_item}
    )


class ActionItemCreateView(LoginRequiredMixin, CreateView):
    model = ActionItem
    fields = ["meeting", "description", "owner", "due_date", "status"]
    template_name = "meetings/actionitem_form.html"
    success_url = reverse_lazy("meeting_list")


@login_required
@permission_required("meetings.can_complete_action_item", raise_exception=True)
def complete_action_item(request, pk):
    action_item = get_object_or_404(ActionItem, pk=pk)
    action_item.status = "completed"
    action_item.save()
    return redirect("meeting_detail", pk=action_item.meeting.pk)
