from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = "temporary.html"

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
