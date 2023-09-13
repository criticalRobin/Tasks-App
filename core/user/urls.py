from django.urls import path
from core.user.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView

app_name = "user"

urlpatterns = [
    path("list/", UserListView.as_view(), name="user_list"),
    path("create/", UserCreateView.as_view(), name="user_create"),
    path("update/<int:pk>/", UserUpdateView.as_view(), name="user_update"),
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="user_delete"),
]
