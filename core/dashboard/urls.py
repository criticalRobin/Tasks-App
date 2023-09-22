from django.urls import path
from core.dashboard.views import DashboardView


app_name = "dashboard"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard_view"),
]
