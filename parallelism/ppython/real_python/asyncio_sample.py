import asyncio


async def hello():
    await asyncio.sleep(2)
    print('hello world')


# async def main():
#     await asyncio.gather(hello())
async def bye():
    await asyncio.sleep(1)
    print('bye world')


async def main():
    asyncio.create_task(bye())
    await hello()


asyncio.run(main())
# asyncio.run(hello())
