from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from accounts.models import Account


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            Account.objects.create_superuser(
                firstname = "admin",
                lastname = "user",
                email = "admin@users.com"
                username='admin',
                password='Django@123'
            )
        print('Superuser has been created.')