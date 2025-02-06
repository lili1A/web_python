from django.apps import AppConfig
from django.contrib.auth import get_user_model

class ProjectsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "projects"

    def ready(self):
        """Create predefined users when the app starts"""
        User = get_user_model()
        users = [
            {"username": "admin", "role": "admin", "password": "admin123"},
            {"username": "manager", "role": "manager", "password": "manager123"},
            {"username": "executor", "role": "executor", "password": "executor123"},
        ]

        for user_data in users:
            if not User.objects.filter(username=user_data["username"]).exists():
                user = User.objects.create(username=user_data["username"], role=user_data["role"])
                user.set_password(user_data["password"])
                user.save()
