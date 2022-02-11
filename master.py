import asyncio
import asyncio.queues
import asyncio.subprocess


class Master:
    def __init__(self):
        self.postconf = '/usr/sbin/postconf'
