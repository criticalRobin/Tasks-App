# Generated by Django 4.2.5 on 2023-09-19 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_alter_group_description_alter_group_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmembership',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.group'),
        ),
        migrations.AlterField(
            model_name='groupmembership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.group'),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
