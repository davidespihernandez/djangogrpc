from django.core.management.base import BaseCommand
from mixer.backend.django import mixer

from msp.models import Token


class Command(BaseCommand):
    help = 'Creates test data for the CPO'

    def handle(self, *args, **options):
        Token.objects.all().delete()
        for i in range(10):
            mixer.blend(Token)
