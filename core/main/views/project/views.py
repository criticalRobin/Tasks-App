from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.main.models import Project
from core.main.forms import ProjectForm


class ProjectListView(ListView):
    model = Project
    template_name = "project/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Projects List"
        context["list_url"] = reverse_lazy("main:project_list")
        context["entity"] = "Projects"
        return context


class ProjectCreateView(CreateView):
    model = Project
    template_name = "project/create.html"
    form_class = ProjectForm
    success_url = reverse_lazy("main:project_list")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return render(request, self.template_name, context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Project"
        context["list_url"] = reverse_lazy("main:project_list")
        context["entity"] = "Projects"
        return context


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "project/create.html"
    success_url = reverse_lazy("main:project_list")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Project Update"
        context["list_url"] = reverse_lazy("main:project_list")
        context["entity"] = "Projects"
        context["form"].fields["project_manager"].widget.attrs["readonly"] = True
        return context


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "project/delete.html"
    success_url = reverse_lazy("main:project_list")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Project Delete"
        context["list_url"] = reverse_lazy("main:project_list")
        context["entity"] = "Projects"
        return context
