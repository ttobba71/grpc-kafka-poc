import grpc
from concurrent import futures
import time

import payload_pb2
import payload_pb2_grpc
import json
from payload_pb2 import *


class DemoService(payload_pb2_grpc.DemogRPCServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetResponseFromPayload(self, request, context):
        print('GetResponseFromPayload called')
        message = json.dumps(request.__str__())
        print(message)
        return payload_pb2.ResponseMessage(response_code=200, response_message='Hello Ruby!!')


def serve():
    print('Staring up on port 50051')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payload_pb2_grpc.add_DemogRPCServicer_to_server(DemoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()