import asyncio
import random

from api import StatsBase, SearchReq, GetStatsResp, StatsEntity
from grpclib.server import Server


class StatsService(StatsBase):
    async def get(self, request: "SearchReq") -> "GetStatsResp":
        print("GetStats Request Made:")
        resource = GetStatsResp()

        for i in range(1, int(request.search)):
            entity = StatsEntity()
            entity.id = i
            entity.username = f'test_username_{i}'
            entity.first_name = f'test_first_name{i}'
            entity.last_name = f'test_last_name{i}'
            entity.cock_size = random.randint(0, 50)
            resource.stats_entities.append(entity)

        print(resource)
        return resource


async def main():
    server = Server([StatsService()])
    await server.start("127.0.0.1", 50051)
    await server.wait_closed()

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
