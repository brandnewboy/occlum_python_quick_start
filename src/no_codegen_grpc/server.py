from concurrent import futures
import grpc

protos, services = grpc.protos_and_services("index.proto")


class HelloXXX(services.HelloServicer):
    def SayHello(self, request, context):
        age = request.age
        name = request.name
        result = f"Hello, {name}! You are {age} years old. xxxxxxxx"
        return protos.HelloResponse(yourName=name, message=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services.add_HelloServicer_to_server(HelloXXX(), server)
    server.add_insecure_port("127.0.0.1:50051")
    server.start()
    print("Server started, listening on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()