import asyncio
import datetime
import requests
import traceback

# random
# async def main():
#     await asyncio.sleep(1)
#     print('hello')
#
# asyncio.run(main())
#
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
#
#
# loop = asyncio.get_event_loop()
#
#

# def print_now():
#     print(datetime.datetime.now())
#
#
# loop.call_soon(print_now)
# loop.call_soon(print_now)
# loop.run_until_complete(asyncio.sleep(5))
#
# def trampoline(name = ""):
#     print(name, end=" ")
#     print_now()
#     loop.call_later(0.5, trampoline, name)
#
# loop.call_soon(trampoline)
# loop.call_later(8, print_now)
#
# loop.run_forever()


# # TODO use async timing methods
# # timing syncronous code
# sync_list = []
#
# def searchApi():
#
#     url = "https://findtreatment.samhsa.gov/locator/listing"
#     sync_page = 0
#
#     try:
#         while True:
#
#             sync_page += 1
#             data = {"sType": "BOTH",
#                     "sAddr": "38.3507711,-85.9100089",
#                     "pageSize": "100",
#                     "page": {sync_page},
#                     "sort": "0"}
#
#             start_req = datetime.datetime.now()
#             response = requests.post(url, data=data)
#             end_req = datetime.datetime.now()
#             single = end_req - start_req
#             print("single response time", single)
#
#             if(response.status_code == 200):
#                 res = response.json()
#                 sync_list.append(res["rows"])
#                 if sync_page == res["totalPages"]:
#                     break
#
#     except Exception:
#         print(traceback.format_exc())
#
# start_sync = datetime.datetime.now()
# searchApi()
# end_sync = datetime.datetime.now()
#
# print(end_sync - start_sync)

# async seems faster want to store the result
# ######################################

import aiohttp
# import json
async_list = []

async def fetch(session, url, data):
    print(data["page"])
    async with session.post(url, data=data) as response:
        print("response", data["page"])
        return await response.json()

async def main(url, data):
    print("main_async", data["page"])
    async with aiohttp.ClientSession() as session:
        print("session", data["page"])
        return await fetch(session, url, data)

page = 0

url = "https://findtreatment.samhsa.gov/locator/listing"

data = {"sType": "BOTH",
        "sAddr": "38.3507711,-85.9100089",
        "pageSize": "100",
        "page": "1",
        "sort": "0"}

response = requests.post(url, data=data)
total_pages = response.json()["totalPages"]

tupes = []

while True:

    page += 1
    data = {"sType": "BOTH",
            "sAddr": "38.3507711,-85.9100089",
            "pageSize": "100",
            "page": f"{page}",
            "sort": "0"}

    if (response.status_code == 200):
        tupes.append((url, data))
        if page >= total_pages:
            break

loop = asyncio.get_event_loop()
task = asyncio.gather(*[main(tupe[0], tupe[1]) for tupe in tupes])

start_async = datetime.datetime.now()
loop.run_until_complete(task)
end_async = datetime.datetime.now()
print(end_async - start_async)

# grequests with gevents

# import grequests
#
# response = grequests.post(url, data=data)
# res = grequests.map([response])
# if(res[0].status_code == 200):
#     total_pages = res[0].json()["totalPages"]
# else:
#     raise Exception("Bad Request")
#
# rs = (grequests.post(u, data=d) for u, d in tupes)
#
# results = grequests.map(rs)
#
# import json
# for each in results:
#     print(json.loads(each.text))



