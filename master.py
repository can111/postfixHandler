import asyncio
import asyncio.queues
import asyncio.subprocess


class Master:
    def __init__(self):
        self.postconf = '/usr/sbin/postconf'
        self.postmap = '/usr/sbin/postmap'

    async def basic_process(self, cmd, params: list) -> (bytes, bytes, int):
        proc = await asyncio.create_subprocess_exec(
            cmd, *params,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
            )
        data, err = await proc.communicate()
        return data, err, proc.returncode

    async def get_postconf(self, info: dict):
        try:
            assert isinstance(info, dict)
            parameter = info['variables']
            args = ['-f', parameter]
        except AssertionError:
            # wrong data input
            return []
        except KeyError:
            # variables not found
            return []
        else:
            output, error, code = await self.basic_process(self.postconf, args)
            return output, error

    async def del_postconf(self, info: dict):
        try:
            assert isinstance(info, dict)
            parameter = info['variables']
            args = ['-#', parameter]
        except AssertionError:
            # wrong data input
            return []
        except KeyError:
            # variables not found
            return []
        else:
            output, error, code = await self.basic_process(self.postconf, args)
            return output, error

    async def put_postconf(self, info: dict):
        try:
            assert isinstance(info, dict)
            args = ['-e']
            for key, value in info.items():
                args.append(f'{key}={value}')
        except AssertionError:
            # wrong data input
            return []
        except KeyError:
            # variables not found
            return []
        else:
            output, error, code = await self.basic_process(self.postconf, args)
            return output, error

    async def get_postmap(self, info: dict):
        try:
            assert isinstance(info, dict)
            parameter = info['variables']
        except AssertionError:
            # wrong data input
            return []
        except KeyError:
            # variables not found
            return []

    async def del_postmap(self, info: dict):
        try:
            assert isinstance(info, dict)
            parameter = info['variables']
        except AssertionError:
            # wrong data input
            return []
        except KeyError:
            # variables not found
            return []

    async def put_postmap(self, info: dict):
        try:
            assert isinstance(info, dict)
        except AssertionError:
            # wrong data input
            return []
        except KeyError:
            # variables not found
            return []
