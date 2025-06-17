import src.datetime_grpc.xxx.datetime_pb2 as datetime_pb2
import src.datetime_grpc.xxx.datetime_pb2_grpc as datetime_pb2_grpc
import grpc
import time
from concurrent import futures

class DatetimeService(datetime_pb2_grpc.DateServicer):
    def GetDate(self, request, context):
        # 'YYYY-MM-DD'
        year = int(time.strftime('%Y', time.localtime(time.time())))
        month = int(time.strftime('%m', time.localtime(time.time())))
        day = int(time.strftime('%d', time.localtime(time.time())))
        result = datetime_pb2.DateResponse(year=year, month=month, day=day)
        msg = request.msg
        print(f"server received msg: {msg}")
        return result


def run_datetime_service():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    datetime_pb2_grpc.add_DateServicer_to_server(DatetimeService(), server)
    server.add_insecure_port('127.0.0.1:50053')
    server.start()
    print('Server started. Listening on port 50053.')
    server.wait_for_termination()


if __name__ == '__main__':
    run_datetime_service()