from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Configuration class for the API application.
    This class is used to configure the API app within the Django project.
    It sets the default auto field type and specifies the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
