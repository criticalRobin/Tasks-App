from django.db.models.signals import post_save
from core.main.models import Group, Task
from django.dispatch import receiver


@receiver(post_save, sender=Group)
def update_project_status(sender, instance, **kwargs):
    project = instance.project
    total_groups = project.group_set.count()
    full_completed_groups = project.group_set.filter(status="Completed").count()

    if total_groups == full_completed_groups:
        project.status = True
    else:
        project.status = False

    project.save()


@receiver(post_save, sender=Task)
def update_group_status(sender, instance, **kwargs):
    group = instance.group
    total_tasks = group.task_set.count()
    full_completed_tasks = group.task_set.filter(status=True).count()

    if total_tasks == full_completed_tasks:
        group.status = "Completed"
    elif full_completed_tasks > 0:
        group.status = "In Progress"
    else:
        group.status = "Not Started"

    group.save()
