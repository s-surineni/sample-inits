import asyncio


async def coro1():
    print('Started coro1')
    await asyncio.sleep(1)
    print('Ended coro1')


async def coro2():
    print('Started coro2')
    await asyncio.sleep(1)
    print('Ended coro2')


async def main():
    await asyncio.gather(
        coro1(),
        coro2())


asyncio.run(main())
