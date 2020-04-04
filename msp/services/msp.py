import logging

from django.db import transaction
from google.protobuf.timestamp_pb2 import Timestamp

import protocol.proto.msp_pb2_grpc
from protocol.proto.msp_pb2_grpc import TokensServicer
from protocol.proto.msp_pb2 import TokenCreationRequest, TokenDetailRequest, TokenListRequest
from protocol.proto.types_pb2 import Token

from msp.models import Token as TokenModel

logger = logging.getLogger(__name__)


def grpc_hook(server):
    protocol.proto.msp_pb2_grpc.add_TokensServicer_to_server(TokensService(), server)


class TokensService(TokensServicer):
    def _model_to_proto(self, token_model: TokenModel):
        date_created = Timestamp()
        date_created.GetCurrentTime()
        date_created.seconds = int(token_model.date_created.timestamp())
        return Token(id=token_model.id, uid=token_model.uid, name=token_model.name, date_created=date_created)

    def GetToken(self, request: TokenDetailRequest, context) -> Token:
        logger.info(f"Called Server GetToken {request}")
        token_model = TokenModel.objects.get(pk=request.id)
        return self._model_to_proto(token_model)

    def GetTokenList(self, request: TokenListRequest, context):
        logger.info(f"Called GetTokenList {request}")
        tokens = TokenModel.objects.all().order_by("pk")[request.offset:request.offset+request.num_items]
        for token_model in tokens:
            yield self._model_to_proto(token_model)

    @transaction.atomic
    def CreateToken(self, request: TokenCreationRequest, context):
        logger.info(f"Called CreateToken {request}")
        token_model = TokenModel.objects.create(
            name=request.name,
            uid=request.uid,
        )
        return self._model_to_proto(token_model)
