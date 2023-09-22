from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.main.models import GroupMembership, Group, User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from core.main.forms import GroupMembershipForm


class GroupMembershipListView(ListView):
    model = GroupMembership
    template_name = "group_membership/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Group Membership List"
        context["list_url"] = reverse_lazy("main:group_membership_list")
        context["entity"] = "Group Membership"
        return context


class GroupMembershipCreateView(CreateView):
    model = GroupMembership
    form_class = GroupMembershipForm
    template_name = "group_membership/create.html"
    success_url = reverse_lazy("main:group_membership_list")

    def post(self, request, **kwargs):
        group_id = kwargs["pk"]
        group = Group.objects.get(id=group_id)
        form = self.form_class(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.group = group
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return render(self, request, self.template_name, context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Group Membership"
        context["list_url"] = reverse_lazy("main:group_membership_list")
        context["entity"] = "Group Membership"
        return context


class GroupMembershipDeleteView(DeleteView):
    model = GroupMembership
    template_name = "group_membership/delete.html"
    success_url = reverse_lazy("main:group_membership_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Group Membership"
        context["list_url"] = reverse_lazy("main:group_membership_list")
        context["entity"] = "Group Membership"
        return context
