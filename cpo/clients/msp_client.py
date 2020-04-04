import logging
from typing import List

import grpc

from functools import lru_cache
from protocol.proto import msp_pb2_grpc
from protocol.proto.types_pb2 import Token
from protocol.proto.msp_pb2 import TokenDetailRequest, TokenListRequest, TokenCreationRequest

logger = logging.getLogger(__name__)


@lru_cache(maxsize=1)
def get_tokens_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = msp_pb2_grpc.TokensStub(channel)
    return stub


def get_token(token_id: int) -> Token:
    logger.info("called client get_token")
    request: TokenDetailRequest = TokenDetailRequest(id=token_id)
    token: Token = get_tokens_client().GetToken(request)
    return token


def get_token_list(offset: int = 0, num_items: int = 3) -> List[Token]:
    logger.info("called client get_token_list")
    request: TokenDetailRequest = TokenListRequest(offset=offset, num_items=num_items)
    tokens: List[Token] = list(get_tokens_client().GetTokenList(request))
    return tokens


def create_token(name: str, uid: str) -> Token:
    logger.info("called client create_token")
    request: TokenCreationRequest = TokenCreationRequest(name=name, uid=uid)
    token: Token = get_tokens_client().CreateToken(request)
    return token
