# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import protocol.proto.msp_pb2 as msp__pb2
import protocol.proto.types_pb2 as types__pb2


class TokensStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTokenList = channel.unary_stream(
                '/cpsp.Tokens/GetTokenList',
                request_serializer=msp__pb2.TokenListRequest.SerializeToString,
                response_deserializer=types__pb2.Token.FromString,
                )
        self.GetToken = channel.unary_unary(
                '/cpsp.Tokens/GetToken',
                request_serializer=msp__pb2.TokenDetailRequest.SerializeToString,
                response_deserializer=types__pb2.Token.FromString,
                )
        self.CreateToken = channel.unary_unary(
                '/cpsp.Tokens/CreateToken',
                request_serializer=msp__pb2.TokenCreationRequest.SerializeToString,
                response_deserializer=types__pb2.Token.FromString,
                )


class TokensServicer(object):
    """Missing associated documentation comment in .proto file"""

    def GetTokenList(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetToken(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateToken(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TokensServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTokenList': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTokenList,
                    request_deserializer=msp__pb2.TokenListRequest.FromString,
                    response_serializer=types__pb2.Token.SerializeToString,
            ),
            'GetToken': grpc.unary_unary_rpc_method_handler(
                    servicer.GetToken,
                    request_deserializer=msp__pb2.TokenDetailRequest.FromString,
                    response_serializer=types__pb2.Token.SerializeToString,
            ),
            'CreateToken': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateToken,
                    request_deserializer=msp__pb2.TokenCreationRequest.FromString,
                    response_serializer=types__pb2.Token.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cpsp.Tokens', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Tokens(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def GetTokenList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/cpsp.Tokens/GetTokenList',
            msp__pb2.TokenListRequest.SerializeToString,
            types__pb2.Token.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cpsp.Tokens/GetToken',
            msp__pb2.TokenDetailRequest.SerializeToString,
            types__pb2.Token.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cpsp.Tokens/CreateToken',
            msp__pb2.TokenCreationRequest.SerializeToString,
            types__pb2.Token.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
