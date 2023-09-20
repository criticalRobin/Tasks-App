from django.urls import path
from core.main.views.project.views import *
from core.main.views.group.views import *
from core.main.views.group_membership.views import *
from core.main.views.task.views import *

app_name = "main"

urlpatterns = [
    # PROJECT URLS
    path("project/list/", ProjectListView.as_view(), name="project_list"),
    path("project/create/", ProjectCreateView.as_view(), name="project_create"),
    path(
        "project/update/<int:pk>/", ProjectUpdateView.as_view(), name="project_update"
    ),
    path(
        "project/delete/<int:pk>/", ProjectDeleteView.as_view(), name="project_delete"
    ),
    # GROUP URLS
    path("group/list/", GroupListView.as_view(), name="group_list"),
    path(
        "project/<int:pk>/group/create/", GroupCreateView.as_view(), name="group_create"
    ),
    path("group/update/<int:pk>/", GroupUpdateView.as_view(), name="group_update"),
    path("group/delete/<int:pk>/", GroupDeleteView.as_view(), name="group_delete"),
    # GROUP MEMBERSHIP URLS
    # TASK URLS
    path("task/list/", TaskListView.as_view(), name="task_list"),
    path("group/<int:pk>/task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),
]
