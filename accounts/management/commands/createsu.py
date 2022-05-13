from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Account


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not Account.objects.filter(username="admin3").exists():
            Account.objects.create_superuser(username="admin3", email="admin3@admin.com", 
                                             password="Django@123", first_name="first", last_name="last")