from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from core.models import Food


class Command(BaseCommand):
    help = ('Updates Food models with new name, description and/or common name using dictionary from ./core/names.py.\n'
            'This will modify records in the database!')

    @transaction.atomic
    def handle(self, *args, **options):
        import core.names as names
        counter = 0
        for id, name_list in names.names.items():
            changed = False
            try:
                food = Food.objects.get(id=id)
            except Exception as e:
                print(id, name_list)
                raise e
            if food.name != name_list[0]:
                food.name = name_list[0]
                changed = True
            if len(name_list) > 1 and food.description != name_list[1]:
                food.description = name_list[1]
                changed = True
            if len(name_list) > 2 and food.common_name != name_list[2]:
                food.common_name = name_list[2]
                changed=True
            if changed:
                counter += 1
                food.save()
        if not counter:
            self.stdout.write('No update was applied. Names are up to date.')
        else:
            self.stdout.write(self.style.SUCCESS('Successfully updated %s food names.' % counter))
