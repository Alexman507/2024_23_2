from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Контент-манагер ннада?"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email="content-manager@sky.pro",
            first_name="Content-manager",
            last_name="SkyPro",
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )

        user.set_password("123")
        user.save()
