from django.apps import AppConfig
# import _profiles.signals 
# (bunu yapamayız çünkü daha apps.py'yi kullanmadan, signals'e erişmeye çalışıyoruz ama signals.py'de models.py kullanılıyor)
# bunun yerine aşağıdaki ready fonksiyonunu yazıyoruz

class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '_profiles'

    def ready(self):
        import _profiles.signals
