
require 'grpc'
require 'payload_pb'

def main
  stub = Payload::DemogRPC::Stub.new('localhost:50051', :this_channel_is_insecure)
  payload_msg = PayloadMessage(name: 'John Doe', id: 1, created: '2020-01-01', cost: 100, id_uuid: '123e4567-e89b-12d3-a456-426655440000')
  print "Payload: #{payload_msg}\n"
  response_msg = stub.get_response_from_payload(payload_msg)
  print "Response: #{response_msg}\n"
end