import logging
from typing import List

from django.core.management.base import BaseCommand

from cpo.clients.msp_client import get_token_list
from protocol.proto.types_pb2 import Token

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Sends a get token list to the MSP server'

    def handle(self, *args, **options):
        offset = int(input("Enter offset (0): ") or 0)
        num_items = int(input("Enter num_items (3): ") or 3)

        tokens: List[Token] = get_token_list(offset=offset, num_items=num_items)
        logger.info(f"received token {tokens}")
