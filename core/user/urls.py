from django.urls import path
from core.user.views import UserListView, UserCreateView

app_name = "user"

urlpatterns = [
    path("list/", UserListView.as_view(), name="user_list"),
    path("create/", UserCreateView.as_view(), name="user_create"),
]
