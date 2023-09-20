from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.main.models import Task, Group, GroupMembership
from core.main.forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = "task/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Tasks List"
        context["list_url"] = reverse_lazy("main:task_list")
        context["entity"] = "Tasks"
        return context


class TaskCreateView(CreateView):
    model = Task
    template_name = "task/create.html"
    form_class = TaskForm
    success_url = reverse_lazy("main:task_list")

    def get(self, request, *args, **kwargs):
        # Obtén el 'group_id' de los argumentos de la URL
        group_id = kwargs["pk"]
        # Obtiene el objeto de grupo asociado con el 'group_id' o muestra un error 404 si no existe
        group = get_object_or_404(Group, pk=group_id)
        # Filtra los objetos de GroupMembership asociados con el grupo específico
        group_membership = GroupMembership.objects.filter(group=group)
        # Filtra nuevamente (esto parece redundante, ya que se filtra anteriormente)
        # y obtén una lista plana de los usuarios asociados con el grupo
        users = group_membership.filter(group=group).values_list("user", flat=True)
        # Crea una instancia del formulario que se utilizará
        form = self.form_class()
        # Establece el queryset del campo 'user' en el formulario para mostrar solo los usuarios del grupo
        form.fields["user"].queryset = users.all()
        # Renderiza la plantilla con el formulario y lo pasa como contexto
        return render(request, self.template_name, context={"form": form})

    def post(self, request, *args, **kwargs):
        group_id = kwargs["pk"]
        group = get_object_or_404(Group, pk=group_id)
        form = self.form_class(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.group = group
            form.save()
            return HttpResponseRedirect(self.success_url)
        print("Erroooooooor")
        self.object = None
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return render(request, self.template_name, context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Task"
        context["list_url"] = reverse_lazy("main:task_list")
        context["entity"] = "Tasks"
        return context


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task/create.html"
    success_url = reverse_lazy("main:task_list")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Task Update"
        context["list_url"] = reverse_lazy("main:task_list")
        context["entity"] = "Tasks"
        return context


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task/delete.html"
    success_url = reverse_lazy("main:task_list")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Task Delete"
        context["list_url"] = reverse_lazy("main:task_list")
        context["entity"] = "Tasks"
        return context
