#! /usr/bin/env python3
# -*- coding : utf-8 -*-

from aiohttp import web
import asyncio
from datetime import datetime
import time
import json
import os
import aiohttp
import logging
logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', '9000')
    print('Server started at http://127.0.0.1:9000')
    await site.start()

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
