import quickfix as fix
import quickfix44 as fix44

import asyncio




async def testing():
    print('Begin of Quickfix testing...')

    await asyncio.sleep(3)
    print("End of quickfix testing.")



async def test_2():
    print("Begin of test 2")
    await asyncio.sleep(1)
    print("End of test_2")

async def main():
    t1 = asyncio.create_task(testing())
    t2 = asyncio.create_task(test_2())
    await t1, t2

asyncio.run(main())