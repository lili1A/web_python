
from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('manager', 'Project Manager'),
        ('executor', 'Executor'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Project(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("finished", "Finished"),
        ("paused", "Paused"),
    ]
    ASSIGNED_TO = [
        ("manager", "Manager"),
        ("not assigned yet", "Not assigned yet"),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="active")
    assigned = models.CharField(max_length=50, choices=ASSIGNED_TO, default = "manager")
    
    def __str__(self):
        return self.title

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]
    
    STATUS_CHOICES = [
        ("not_started", "Not Started"),
        ("started", "Started"),
        ("finished", "Finished"),
    ]
    
    ASSIGNED_TO = [
        ("executor", "Executor"),
        ("manager", "Manager"),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="medium")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="not_started")
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    assigned = models.CharField(max_length=50, choices=ASSIGNED_TO, default = "manager")
    
    def __str__(self):
        return self.title


