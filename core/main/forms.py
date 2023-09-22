from django import forms
from core.main.models import *


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["name"].widget.attrs["autofocus"] = True
        self.fields["start_date"].widget = forms.DateInput(attrs={"type": "date"})
        self.fields["end_date"].widget = forms.DateInput(attrs={"type": "date"})

    class Meta:
        model = Project
        fields = ["name", "description", "start_date", "end_date", "project_manager"]
        labels = {
            "name": "Project Name",
            "description": "Project Description",
            "start_date": "Project Start Date",
            "end_date": "Project End Date",
            "project_manager": "Project Manager",
        }


class GroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["name"].widget.attrs["autofocus"] = True

    class Meta:
        model = Group
        fields = ["name", "description", "status"]
        labels = {
            "name": "Group Name",
            "description": "Group Description",
            "status": "Group Status",
        }


class GroupMembershipForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
        self.fields["user"].widget.attrs["autofocus"] = True

    class Meta:
        model = GroupMembership
        fields = ["user"]
        labels = {
            "user": "User",
        }


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["name"].widget.attrs["autofocus"] = True
        self.fields["start_date"].widget = forms.DateInput(attrs={"type": "date"})
        self.fields["end_date"].widget = forms.DateInput(attrs={"type": "date"})

    class Meta:
        model = Task
        fields = ["name", "description", "start_date", "end_date", "user"]
        labels = {
            "name": "Task Name",
            "description": "Task Description",
            "start_date": "Task Start Date",
            "end_date": "Task End Date",
            "user": "User",
        }
