from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from meetings import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("meetings/", views.meeting_list, name="meeting_list"),
    path("meetings/<int:pk>/", views.meeting_detail, name="meeting_detail"),
    path("meetings/create/", views.MeetingCreateView.as_view(), name="meeting_create"),
    path(
        "meetings/<int:pk>/update/",
        views.MeetingUpdateView.as_view(),
        name="meeting_update",
    ),
    path(
        "meetings/<int:pk>/delete/",
        views.MeetingDeleteView.as_view(),
        name="meeting_delete",
    ),
    path("action-items/<int:pk>/", views.action_item_detail, name="action_item_detail"),
    path(
        "action-items/<int:pk>/complete/",
        views.complete_action_item,
        name="complete_action_item",
    ),
]
