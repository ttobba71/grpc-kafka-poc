# GRPC
- `protos/payload.proto` This is the contract between the client and the server.  This will be in a separate project and will have dedicated process to generate a gem or a pypi package when it's versioned.
- `main.py`  This has example code starting up the grpc server.  We want ssl, robust error handling and recovery logic if the process dies. 
- `payload_pb2.py` The generated protocal buffer. This file and the `_grpc` file are both generated from the `.proto` file.
- `payload_pg2_grpc.py` This generated file is the client/server classes.  It supports communicating with the previously generated protocol buffer.
- `protobuf_to_dict.py` This is a convenience package.  I found it online.  It hadn't been updated to support recent python 3.x changes, so I grabbed the file and updated the code.  We may decide to update the repo or we can to create a internal package so we can evolve it for our needs faster. 




The following command will generate the `_pb2` files for the pythong programming language.
`python -m grpc_tools.protoc --proto_path=protos payload.proto --python_out=.  --grpc_python_out=.`

# Kafka
- `messaging-client.ini` This file is the configuration file for the messaging client.  This is currently still be updated.  It does work, however, the messaging-client package readme.md is missing documentation.  I've been troubleshooting and fleshing out the different config file variables in a separate repository.  *More to come on this...*
- `api-key-TRLVFID3FJQ23BSH.txt` I downloaded the confluent-cloud key/secret to this file.  It's for the development environment. 