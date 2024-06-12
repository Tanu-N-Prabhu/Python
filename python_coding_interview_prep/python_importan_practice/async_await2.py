import asyncio

async def async_foo():
    """
    Asynchronous function that prints a message, waits for 5 seconds, then prints another message.
    """
    print("async_foo started")
    await asyncio.sleep(5)
    print("async_foo done")

async def main():
    """
    Main asynchronous function that schedules 'async_foo' to run concurrently and performs actions before and after it.
    """
    print('Do some actions 0 calling async_foo()')
    asyncio.ensure_future(async_foo())  # fire and forget async_foo()
    print('Do some actions 1')
    await asyncio.sleep(5)
    print('Do some actions 2')


if __name__ == '__main__':
    # Create the event loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close
    print('Done')
