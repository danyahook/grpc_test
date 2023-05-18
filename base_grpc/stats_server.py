import grpc
import random

import stats_pb2
import stats_pb2_grpc

from concurrent import futures


class StatsServicer(stats_pb2_grpc.StatsServicer):
    def Get(self, request, context):
        print("GetStats Request Made:")
        stats_res = stats_pb2.GetStatsResp()

        for i in range(1, int(request.search)):
            entity = stats_pb2.StatsEntity()
            entity.id = i
            entity.Username = f'test_username_{i}'
            entity.FirstName = f'test_first_name{i}'
            entity.LastName = f'test_last_name{i}'
            entity.CockSize = random.randint(0, 50)
            stats_res.statsEntities.append(entity)

        print(stats_res)
        return stats_res


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stats_pb2_grpc.add_StatsServicer_to_server(StatsServicer(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    print('*** SERVER STARTED ***')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
