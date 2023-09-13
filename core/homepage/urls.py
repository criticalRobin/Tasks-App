from django.urls import path
from core.homepage.views import HomePageView

app_name = "homepage"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
