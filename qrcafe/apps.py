# apps.py dosyası
from django.apps import AppConfig

class QrcafeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'qrcafe'

    def ready(self):
        import qrcafe.signals