from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.main.models import Task
from core.main.forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = "task/list.html"

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self, request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Tasks List"
        context["list_url"] = reverse_lazy("main:task_list")
        context["entity"] = "Tasks"
        return super().get_context_data(**kwargs)


class TaskCreateView(CreateView):
    model = Task
    template_name = "task/create.html"
    form_class = TaskForm
    success_url = reverse_lazy("main:task_list")

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
        context["title"] = "Create Task"
        context["list_url"] = reverse_lazy("main:task_list")
        context["entity"] = "Tasks"
        return super().get_context_data(**kwargs)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task/create.html"
    success_url = reverse_lazy("main:task_list")

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self, request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Task Update"
        context["list_url"] = reverse_lazy("main:task_list")
        context["entity"] = "Tasks"
        context["form"].fields["group"].widget.attrs["readonly"] = True
        context["form"].fields["user"].widget.attrs["readonly"] = True
        return super().get_context_data(**kwargs)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task/delete.html"
    success_url = reverse_lazy("main:task_list")

    @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self, request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Task Delete"
        context["list_url"] = reverse_lazy("main:task_list")
        context["entity"] = "Tasks"
        return super().get_context_data(**kwargs)
