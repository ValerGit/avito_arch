# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import grpcService_pb2 as grpcService__pb2


class salesExchangeStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetPrice = channel.unary_unary(
        '/salesExchange/GetPrice',
        request_serializer=grpcService__pb2.PriceRequest.SerializeToString,
        response_deserializer=grpcService__pb2.PriceResponse.FromString,
        )


class salesExchangeServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetPrice(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_salesExchangeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetPrice': grpc.unary_unary_rpc_method_handler(
          servicer.GetPrice,
          request_deserializer=grpcService__pb2.PriceRequest.FromString,
          response_serializer=grpcService__pb2.PriceResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'salesExchange', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
