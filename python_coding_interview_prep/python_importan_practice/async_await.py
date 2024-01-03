import asyncio
import time


# eg. 1
async def main():
	start = time.time()
	print('hello')
	await asyncio.sleep(.1)
	print('world')

# asyncio.run(main())

# eg. 2
# async def count():
#     print("One")
#     await asyncio.sleep(1)
#     print("Two")

# async def main():
#     await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
