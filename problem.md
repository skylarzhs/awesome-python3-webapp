# 记录执行过程中遇到的问题

## Day4

运行 Model 实例化

1. 执行方法

```
loop = asyncio.get_event_loop()


async def test(loop):
    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome',host='localhost')
    u = User(name='Test', email="test@123.com",
             passwd="123456", image="about:blank")
    await u.save()


loop.run_until_complete(test(loop))
```

原方法没有loop参数，需要通过 `get_event_loop` 获取当前时间循环。

2. ORM 修改

orm 中的创建数据库连接池中的字符集设置修改为 `charset=kw.get('charset', 'utf8')`。

orm 中的 `save` 方法修改主键值的位置，用insert。
