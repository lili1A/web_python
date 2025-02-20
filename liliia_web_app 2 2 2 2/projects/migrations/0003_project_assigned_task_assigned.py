# Generated by Django 5.1.2 on 2025-02-05 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_name_project_title_remove_project_manager_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='assigned',
            field=models.CharField(choices=[('manager', 'Manager'), ('not assigned yet', 'Not assigned yet')], default='manager', max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='assigned',
            field=models.CharField(choices=[('executor', 'Executor'), ('manager', 'Manager')], default='manager', max_length=50),
        ),
    ]
