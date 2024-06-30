from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда для создания модератора"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email='moderator@sky.pro',
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )

        user.set_password('123')
        user.save()
