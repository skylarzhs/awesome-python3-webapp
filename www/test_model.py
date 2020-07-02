#! /usr/bin/env python3
# -*- coding : utf-8 -*-

import asyncio
import orm
import functools
from models import User, Blog, Comment


loop = asyncio.get_event_loop()

# def create_connection(func):
#     @functools.wraps(func)
#     def wrappers(func):
#        ret = func()
#        return ret
#     return wrappers
     
async def test_insert(loop):
    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email="test2@123.com",
             passwd="123456", image="about:blank")
    await u.save()


async def test_del(loop):
    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    u = User(id='0015936784619625c8979b4689249b3a8f4f1c12d4127b6000')
    await u.remove()


async def test_update(loop):
    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    u = User(id='0015936784619625c8979b4689249b3a8f4f1c12d4127b6000', name='modify')
    await u.update()


async def test_find(loop):
    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    u = User()
    await u.find(pk='0015936784619625c8979b4689249b3a8f4f1c12d4127b6000')


async def test_findall(loop):
    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    u = User()
    await u.findAll()

tasks = [
    # test_insert(loop),
    # test_update(loop),
    test_find(loop),
    test_findall(loop),
    test_del(loop),
]
loop.run_until_complete(asyncio.wait(tasks))
