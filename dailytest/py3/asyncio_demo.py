#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xumamba
# @DateTime: 2020/11/23
# @Description:

import asyncio
import time


async def hello(s: int, name: str) -> None:
    print("Hello: ", name)
    await asyncio.sleep(s)
    print("Bye~, ", name)


async def main():
    start = time.perf_counter()
    await asyncio.gather(hello(2, "Jerry"), hello(2, "Tom"))  # gather将多个异步任务包装成一个新的异步任务
    print("execution time: ", time.perf_counter() - start)


asyncio.run(main())

from pyppeteer import launch


async def pyppeteer_test():
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://xumamba.netlify.app/")
    await page.screenshot({'path': 'my_blog.png'})
    await browser.close()

asyncio.run(pyppeteer_test())


import aiohttp

async def http_request(url: str):
    async with aiohttp.ClientSession as session:
        async with session.get(url) as response:
            response = await response.read()
            print(response)

if __name__ == '__main__':
    asyncio.run(http_request('https://www.baidu.com/'))
