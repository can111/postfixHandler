import asyncio
import asyncio.queues
import asyncio.subprocess


class Master:
    def __init__(self):
        self.postconf = '/usr/sbin/postconf'

    async def basic_process(self, cmd, params: list) -> (bytes, bytes, int):
        pass

    async def get_postconf(self, info: dict):
        pass

    async def del_postconf(self, info: dict):
        pass

    async def put_postconf(self, info: dict):
        pass

