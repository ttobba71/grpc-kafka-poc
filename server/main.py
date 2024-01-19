import datetime

import grpc
from concurrent import futures

import payload_pb2
import payload_pb2_grpc
import json
import datetime

from copy import copy
from google.protobuf.descriptor import FieldDescriptor
from protobuf_to_dict import protobuf_to_dict, TYPE_CALLABLE_MAP


type_callable_map = copy(TYPE_CALLABLE_MAP)
type_callable_map[FieldDescriptor.TYPE_BYTES] = str

class DemoService(payload_pb2_grpc.DemogRPCServicer):

    def __init__(self, *args, **kwargs):
        pass


    def GetResponseFromPayload(self, request, context):
        print(f'GetResponseFromPayload called - {datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")}')
        req_dict = protobuf_to_dict(request)
        print( f'id-{req_dict["id"]} --- {req_dict}')
        return payload_pb2.ResponseMessage(id=req_dict["id"], response_code=200, response_message=f'Hello Ruby from '
                                                                                              f'Python!! Processed '
                                                                                              f'id: {req_dict["id"]}')


def serve():
    print('Staring up on port 8088')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payload_pb2_grpc.add_DemogRPCServicer_to_server(DemoService(), server)
    server.add_insecure_port('[::]:8088')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
