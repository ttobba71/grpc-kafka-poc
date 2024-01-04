
- `protos/payload.proto`
- `main.py`
- `payload_pb2.py`
- `payload_pg2_grpc.py`





`python -m grpc_tools.protoc --proto_path=protos payload.proto --python_out=.  --grpc_python_out=.`