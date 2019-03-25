from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from core.models import Food

from pathlib import Path

class Command(BaseCommand):
    help = 'Updates Food table with new common names from ./core/commonnames.py'

    @transaction.atomic
    def handle(self, *args, **options):
        import core.commonnames as commonnames
        counter = 0
        for id, name in commonnames.common_names.items():
            food = Food.objects.get(id=id)
            if food.common_name != name:
                food.common_name = name
                food.save()
                counter += 1
        if not counter:
            self.stdout.write('No update was applied. Common names are up to date.')
        else:
            self.stdout.write(self.style.SUCCESS('Successfully updated %s food common names.' % counter))