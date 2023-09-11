from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.main.models import Group
from core.main.forms import GroupForm


class GroupListView(ListView):
    model = Group
    template_name = "group/list.html"

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self, request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Groups List"
        context["list_url"] = reverse_lazy("main:group_list")
        context["entity"] = "Groups"
        return super().get_context_data(**kwargs)


class GroupCreateView(CreateView):
    model = Group
    template_name = "group/create.html"
    form_class = GroupForm
    success_url = reverse_lazy("main:group_list")

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return render(request, self.template_name, context)

    def get_context_date(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Group"
        context["list_url"] = reverse_lazy("main:group_list")
        context["entity"] = "Groups"
        return super().get_context_data(**kwargs)


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = "group/create.html"
    success_url = reverse_lazy("main:group_list")

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self, request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Group Update"
        context["list_url"] = reverse_lazy("main:group_list")
        context["entity"] = "Groups"
        return super().get_context_data(**kwargs)


class GroupDeleteView(DeleteView):
    model = Group
    template_name = "group/delete.html"
    success_url = reverse_lazy("main:group_list")

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self, request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Group Delete"
        context["list_url"] = reverse_lazy("main:group_list")
        context["entity"] = "Groups"
        return super().get_context_data(**kwargs)
