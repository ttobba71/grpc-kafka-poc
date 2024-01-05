
require 'grpc'
require_relative 'payload_services_pb'
require_relative 'payload_pb'

puts "test-before-main"
def main
  puts "test"
  stub = DemogRPC::Stub.new('localhost:50051', :this_channel_is_insecure)
  payload_msg = PayloadMessage.new(customer_name: 'John Doe', id: 1, created: '2020-01-01', cost: 100, id_uuid: '123e4567-e89b-12d3-a456-426655440000')
  puts "Payload: #{payload_msg}\n"
  response_msg = stub.get_response_from_payload(payload_msg)
  print "Response: #{response_msg}\n"
end


main