import grpc

import stats_pb2
import stats_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = stats_pb2_grpc.StatsStub(channel)
        stat_request = stats_pb2.SearchReq(search='10')
        stat_reply = stub.Get(stat_request)
        print("GetStats Response Made:")
        print(stat_reply)


if __name__ == '__main__':
    run()
