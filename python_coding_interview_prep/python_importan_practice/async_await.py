import asyncio
import time

# Example 1
async def main1():
    """
    Demonstrates a basic async function.
    """
    start = time.time()
    print(f'hello {start}')
    await asyncio.sleep(.1)
    print('world')

# asyncio.run(main1())

# Example 2
async def count():
    """
    Prints numbers asynchronously.
    """
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main2():
    """
    Runs multiple 'count' coroutines concurrently.
    """
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    asyncio.run(main1())
    start_time = time.perf_counter()
    asyncio.run(main2())
    elapsed_time = time.perf_counter() - start_time
    print(f"{__file__} executed in {elapsed_time:0.2f} seconds.")
