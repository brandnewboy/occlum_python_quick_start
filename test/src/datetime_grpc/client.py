import xxx.datetime_pb2_grpc as datetime_pb2_grpc
import grpc
import xxx.datetime_pb2 as datetime_pb2


if __name__ == '__main__':
    conn = grpc.insecure_channel("localhost:50053")
    client = datetime_pb2_grpc.DateStub(conn)
    request_data = datetime_pb2.DateRequest(msg="hello, I'm client")
    response = client.GetDate(request_data)
    print(response)

