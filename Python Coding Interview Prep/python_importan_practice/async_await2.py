import asyncio


async def async_foo():
    print("async_foo started")
    await asyncio.sleep(5)
    print("async_foo done")

async def main():
    asyncio.ensure_future(async_foo())  # fire and forget async_foo()
    print('Do some actions 1')
    await asyncio.sleep(5)
    print('Do some actions 2')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())