from django import forms
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date', 'assigned', 'status']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status', 'start_date', 'end_date', 'assigned', 'project']
        
class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["status"]  