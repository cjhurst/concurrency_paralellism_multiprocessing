import asyncio


async def main():
    await asyncio.sleep(1)
    print('hello')


asyncio.run(main())

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


loop = asyncio.get_event_loop()


import datetime
def print_now():
    print(datetime.datetime.now())


loop.call_soon(print_now)
loop.call_soon(print_now)
loop.run_until_complete(asyncio.sleep(5))

def trampoline(name = ""):
    print(name, end=" ")
    print_now()
    loop.call_later(0.5, trampoline, name)

loop.call_soon(trampoline)
loop.call_later(8, print_now)

loop.run_forever()


