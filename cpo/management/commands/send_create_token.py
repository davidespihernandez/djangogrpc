import logging

from django.core.management.base import BaseCommand

from cpo.clients.msp_client import create_token
from protocol.proto.types_pb2 import Token

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Sends a create token to the MSP server'

    def handle(self, *args, **options):
        name = input("Enter name ('my name'): ") or "my name"
        uid = input("Enter uid ('111'): ") or "111"

        token: Token = create_token(name=name, uid=uid)
        logger.info(f"received token {token}")
