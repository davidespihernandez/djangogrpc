import logging
from django.core.management.base import BaseCommand

from cpo.clients.msp_client import get_token
from protocol.proto.types_pb2 import Token

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Sends a get token to the MSP server'

    def handle(self, *args, **options):
        token_id = int(input("Enter the token id: "))
        token: Token = get_token(token_id)
        logger.info(f"received token {token}")
