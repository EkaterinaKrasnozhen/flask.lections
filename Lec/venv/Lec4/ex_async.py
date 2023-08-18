import asyncio


async def print_numbers(): # карутины
    for i in range(10):
        print(i)
        await asyncio.sleep(1) # могу подождать, другие могут использовать ресурс


async def print_letters():# карутины
    for letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        print(letter)
        await asyncio.sleep(0.5)


async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_letters())
    await task1 # запускаем первую и если она готова подождать будет 2ая
    await task2
    
    
asyncio.run(main())