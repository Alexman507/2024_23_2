from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда для создания суперпользователя"""

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='nerocross@gmail.com',
            first_name='Admin',
            last_name='Admin',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )

        user.set_password('123')
        user.save()
