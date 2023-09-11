from django.contrib import admin
from core.main.models import Project, Group, GroupMembership, Task

# Register your models here.
admin.site.register(Project)
admin.site.register(Group)
admin.site.register(GroupMembership)
admin.site.register(Task)
