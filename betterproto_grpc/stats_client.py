import asyncio
import betterproto

from api import StatsStub, SearchReq
from grpclib.client import Channel


async def main():
    channel = Channel(host="127.0.0.1", port=50051)
    service = StatsStub(channel)
    request = await service.get(SearchReq(search='10'))
    print(request.to_dict(casing=betterproto.Casing.SNAKE))
    # don't forget to close the channel when done!
    channel.close()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass

