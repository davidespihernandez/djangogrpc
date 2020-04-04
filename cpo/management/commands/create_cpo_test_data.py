from django.core.management.base import BaseCommand
from mixer.backend.django import mixer

from cpo.models import Location


class Command(BaseCommand):
    help = 'Creates test data for the CPO'

    def handle(self, *args, **options):
        Location.objects.all().delete()
        for i in range(10):
            mixer.blend(Location)
