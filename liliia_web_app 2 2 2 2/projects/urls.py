from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    
    # Dashboards
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("manager_dashboard/", views.manager_dashboard, name="manager_dashboard"),
    path("executor_dashboard/", views.executor_dashboard, name="executor_dashboard"),

    # Admin Project Management
    path("project/create/", views.create_project, name="create_project"),
    path("project/edit/", views.edit_project, name="edit_project"),
    path("project/delete/", views.delete_project, name="delete_project"),

    # Admin Task Management
    path("task/create/", views.create_task, name="create_task"),
    path("task/edit/", views.edit_task, name="edit_task"),
    path("task/delete/", views.delete_task, name="delete_task"),

    # Manager Project Management
    path("manager/project/create/", views.mng_create_project, name="mng_create_project"),
    path("manager/project/edit/", views.mng_edit_project, name="mng_edit_project"),
    path("manager/project/delete/", views.mng_delete_project, name="mng_delete_project"),

    # Manager Task Management
    path("manager/task/create/", views.mng_create_task, name="mng_create_task"),
    path("manager/task/edit/", views.mng_edit_task, name="mng_edit_task"),
    path("manager/task/delete/", views.mng_delete_task, name="mng_delete_task"),
    
    
    #  Executor Task Management
    path("executor_dashboard/", views.executor_dashboard, name="executor_dashboard"),
    path("task/update_status/<int:task_id>/", views.update_task_status, name="update_task_status"),

]


    