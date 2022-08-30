import csv
from random import randint

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from auth_app.models import Profile


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        with open(f"{settings.BASE_DIR}/auth_app/management/commands/user.csv", 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            with transaction.atomic():
                for line in reader:
                    suffix = ''.join([str(randint(0, 9)) for _ in range(4)])
                    _, _, tg_id, tg_name, full_name, _, _, _ = line
                    user = User.objects.create(
                        username=tg_name + suffix,
                        password=settings.DEFAULT_USER_PASSWORD
                    )
                    Profile.objects.create(
                        user=user,
                        tg_name=tg_name,
                        tg_id=tg_id,
                        organization_id=1,
                        department_id=2,
                        surname=full_name
                    )
