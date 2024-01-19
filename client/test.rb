
require 'grpc'
require_relative 'payload_services_pb'
require_relative 'payload_pb'

puts "test-before-main"

def main
  puts "Enter 0 to end or a number to run that many times: "
  stub = DemogRPC::Stub.new('localhost:8088', :this_channel_is_insecure)
  x = 1
  while x > 0
    starting = Time.now
    (1..x).each do |i|
      puts "i: #{i}"
      payload_msg = PayloadMessage.new(customer_name: 'John Doe', id: i, created: '2020-01-01', cost: 100, id_uuid: '123e4567-e89b-12d3-a456-426655440000')
      puts "Payload: #{payload_msg}\n"
      response = stub.get_response_from_payload(payload_msg)
      print "Response: #{response.response_message}\n"
    end
    ending = Time.now
    elapsed = ending - starting
    puts "elapsed time: #{elapsed}"
    x = gets.chomp.to_i
  end

end


main