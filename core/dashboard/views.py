from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.user.models import MyUser as User
from core.main.models import Project, Task, GroupMembership
import datetime


# Create your views here.
@method_decorator(
    login_required(login_url=reverse_lazy("login:login_view")), name="dispatch"
)
class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = User.objects.get(username=self.request.user)
        context["projects"] = Project.objects.filter(project_manager=context["user"])
        context["projects_name"] = [project.name for project in context["projects"]]
        context["date"] = datetime.date.today()
        context["today_tasks"] = Task.objects.filter(
            user=context["user"], end_date=context["date"]
        )
        context["group_membership"] = GroupMembership.objects.filter(
            user=context["user"]
        )
        context["groups"] = [group.group for group in context["group_membership"]]
        return context
