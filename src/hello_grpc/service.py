import hello_pb2 as hello_pb2
import hello_pb2_grpc as hello_pb2_grpc
import grpc
from concurrent import futures

class HelloService(hello_pb2_grpc.HelloServiceServicer):
    def SayHello(self, request, context):
        name = request.name
        age = request.age
        result = f"Hello, {name}! You are {age} years old."
        return hello_pb2.HelloResponse(yourName=name, message=result)


def run_hello_service():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServiceServicer_to_server(HelloService(), server)
    server.add_insecure_port('127.0.0.1:9003')
    server.start()
    print("Server started, listening on port 9003")
    server.wait_for_termination()

if __name__ == "__main__":
    run_hello_service()