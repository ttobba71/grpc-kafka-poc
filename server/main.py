import datetime

import grpc
from concurrent import futures
import time

import payload_pb2
import payload_pb2_grpc
import json
import datetime

import asyncio
from avant.messaging import Driver

from payload_pb2 import *


# import dataclasses
# import logging
# import uuid
# from super_cereal.cerealizer.encryption import Encrypted
# from avant.messaging import Driver


class KafkaDemo:
    producer_name = 'risk_determination_request'

    def __init__(self, config_path):
        self.config_path = config_path

    async def produce_msg_to_topic(self, message):
        driver: Driver = Driver.driver_from_config(self.config_path)
        async with driver.producer(self.producer_name) as producer:
            await producer.send(key=message.id, msg=message)


class DemoService(payload_pb2_grpc.DemogRPCServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetResponseFromPayload(self, request, context):
        print(f'GetResponseFromPayload called - {datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")}')
        message = json.dumps(request.__str__())
        print(message)
        kd = KafkaDemo("./messaging-client.ini")
        asyncio.run(kd.produce_msg_to_topic(message))
        return payload_pb2.ResponseMessage(response_code=200, response_message='Hello Ruby!!')


def serve():
    print('Staring up on port 8088')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payload_pb2_grpc.add_DemogRPCServicer_to_server(DemoService(), server)
    server.add_insecure_port('[::]:8088')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
