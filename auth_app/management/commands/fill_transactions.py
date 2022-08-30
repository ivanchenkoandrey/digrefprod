import csv
import datetime
import logging
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from auth_app.models import Transaction


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        users = User.objects.prefetch_related('profile')
        users_data = {user.profile.tg_id: user.pk for user in users}
        with open(f"{settings.BASE_DIR}/auth_app/management/commands/transactions.csv", 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            with transaction.atomic():
                for line in reader:
                    _, created_at, updated_at, sender, recipient, amount, reason, _, _, is_anonymous = line
                    logger.info(f"{created_at=}, {updated_at=}, "
                                f"{sender=}, {recipient=}, {amount=}, "
                                f"{reason=}, {is_anonymous=}")
                    if users_data.get(sender) == 10000:
                        _transaction = Transaction(
                            sender=User.objects.get(pk=users_data.get('10000')),
                            recipient=User.objects.get(pk=users_data.get(str(recipient))),
                            amount=int(amount),
                            reason=reason,
                            is_anonymous=True if int(is_anonymous) else False,
                            transaction_class='E',
                            created_at=datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S.%f'),
                            updated_at=datetime.datetime.strptime(updated_at, '%Y-%m-%d %H:%M:%S.%f'),
                            period_id=2,
                            status='R'
                        )
                        _transaction.save()
                    else:
                        _transaction = Transaction(
                            sender=User.objects.get(pk=users_data.get(str(sender))),
                            recipient=User.objects.get(pk=users_data.get(str(recipient))),
                            amount=int(amount),
                            reason=reason,
                            is_anonymous=True if int(is_anonymous) else False,
                            transaction_class='T',
                            created_at=datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S.%f'),
                            updated_at=datetime.datetime.strptime(updated_at, '%Y-%m-%d %H:%M:%S.%f'),
                            period_id=2,
                            status='R'
                        )
                        _transaction.save()
