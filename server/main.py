import grpc
from concurrent import futures
import time

import payload_pb2_grpc


class DemoService(payload_pb2_grpc.DemogRPCServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetResponseFromPayload(self, request, context):
        message = request.payload_message


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payload_pb2_grpc.add_DemogRPCServicer_to_server(DemoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()