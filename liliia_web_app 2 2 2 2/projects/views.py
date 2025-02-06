 

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Project, Task
from .decorators import role_required
from .forms import ProjectForm, TaskForm, TaskStatusForm

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.role == "admin":
                return redirect("admin_dashboard")
            elif user.role == "manager":
                return redirect("manager_dashboard")
            else:
                return redirect("executor_dashboard")
    return render(request, "management/login.html")

@login_required
@role_required('admin')
def admin_dashboard(request):
    
    projects = Project.objects.all()  
    tasks = Task.objects.all()  
    return render(request, "management/admin_dashboard.html", {"projects": projects, "tasks": tasks})

@login_required
@role_required('admin')
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_dashboard")
    else:
        form = ProjectForm()
    return render(request, "management/create_project.html", {"form": form})

@login_required
@role_required('admin')
def edit_project(request):
    # Get the first project in the database 
    project = Project.objects.first()  # at least one project

    if not project:
        return redirect("admin_dashboard")  

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)  
        if form.is_valid():
            form.save()  
            return redirect("admin_dashboard")  
    else:
        form = ProjectForm(instance=project)  

    return render(request, "management/edit_project.html", {"form": form, "project": project})

@login_required
@role_required('admin')
def delete_project(request):
    
    project = Project.objects.first()  

    if not project:
        return redirect("admin_dashboard")  

    if request.method == "POST":
        project.delete()  
        return redirect("admin_dashboard")  

    return render(request, "management/project_confirm_delete.html", {"project": project})


@login_required
@role_required('admin')
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            tasks = Task.objects.all()  
            projects = Project.objects.all()  
            return render(request, "management/admin_dashboard.html", {"tasks": tasks, "projects": projects, "form": form})
    else:
        form = TaskForm()

    return render(request, "management/create_task.html", {"form": form})

@login_required
@role_required('admin')
def edit_task(request):
    
    task = Task.objects.first()  

    if not task:
      
        return redirect("admin_dashboard")

    if request.method == "POST":
        
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  
            return redirect("admin_dashboard")  
    else:
        
        form = TaskForm(instance=task)

    return render(request, "management/edit_task.html", {"form": form, "task": task})

    
@login_required
@role_required('admin')
def delete_task(request):
    task = Task.objects.first() 

    if not task:
        return redirect("admin_dashboard")  

    if request.method == "POST":
        task.delete()  
        return redirect("admin_dashboard") 

    return render(request, "management/task_confirm_delete.html", {"task": task})

################################################

@login_required
@role_required('manager')
def manager_dashboard(request):
    projects = Project.objects.filter(assigned="manager")  
    tasks = Task.objects.filter(assigned="manager")
    return render(request, "management/manager_dashboard.html", {"projects": projects, "tasks": tasks})

@login_required
@role_required('manager')
def mng_create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manager_dashboard")
    else:
        form = ProjectForm()
    return render(request, "management/mng_create_project.html", {"form": form})

@login_required
@role_required('manager')
def mng_edit_project(request):
    
    project = Project.objects.first()  

    if not project:
        return redirect("manager_dashboard")  

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)  
        if form.is_valid():
            form.save()  
            return redirect("manager_dashboard")  
    else:
        form = ProjectForm(instance=project) 

    return render(request, "management/mng_edit_project.html", {"form": form, "project": project})

@login_required
@role_required('manager')
def mng_delete_project(request):
    
    project = Project.objects.first()  

    if not project:
        return redirect("manager_dashboard")  

    if request.method == "POST":
        project.delete()  
        return redirect("manager_dashboard")  

    return render(request, "management/mng_confirm_delete_project.html", {"project": project})

@login_required
@role_required('manager')
def mng_create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            tasks = Task.objects.filter(assigned="manager")  
            projects = Project.objects.filter(assigned="manager")
            return render(request, "management/manager_dashboard.html", {"tasks": tasks, "projects": projects, "form": form})
    else:
        form = TaskForm()

    return render(request, "management/mng_create_task.html", {"form": form})

@login_required
@role_required('manager')
def mng_edit_task(request):

    task = Task.objects.first() 
    projects = Project.objects.filter(assigned="manager")
    if not task and projects:
       
        return redirect("manager_dashboard")

    if request.method == "POST":
        
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  
            return redirect("manager_dashboard")  
    else:

        form = TaskForm(instance=task)

    return render(request, "management/mng_edit_task.html", {"form": form, "task": task})

@login_required
@role_required('manager')
def mng_delete_task(request):
    task = Task.objects.first()  

    if not task:
        return redirect("admin_dashboard") 

    if request.method == "POST":
        task.delete()  
        return redirect("manager_dashboard")  
    return render(request, "management/mng_confirm_delete_task.html", {"task": task})



################################################
@login_required
@role_required('executor')
def executor_dashboard(request):
    return render(request, "management/executor_dashboard.html")

@login_required
@role_required('executor')
def executor_dashboard(request):
    tasks = Task.objects.filter(assigned="executor")  
    return render(request, "management/executor_dashboard.html", {"tasks": tasks})

@login_required
@role_required('executor')
def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, assigned="executor")  

    if request.method == "POST":
        form = TaskStatusForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("executor_dashboard")  

    else:
        form = TaskStatusForm(instance=task)

    return render(request, "management/update_task_status.html", {"form": form, "task": task})


################################################
def logout_view(request):
    logout(request)
    return redirect("login")
