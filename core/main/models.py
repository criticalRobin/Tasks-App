from django.db import models
from core.user.models import MyUser as User


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add=False)
    status = models.BooleanField(default=False)
    project_manager = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.project_manager}"


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    members = models.ManyToManyField(User, through="GroupMembership")
    STATUS_CHOICES = (
        ("Not Started", "Not Started"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="Not Started"
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.project}"


class GroupMembership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.group}"


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add=False)
    status = models.BooleanField(default=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.group}"
