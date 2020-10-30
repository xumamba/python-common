#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xulp
# @DateTime: 2020/10/28 15:57
# @Description:
import mock


class Foo(object):
    def echo(self, *args):
        return 'hello'


def some_function():
    foo = Foo()
    return foo.echo()


with mock.patch('__main__.Foo') as foo_mock:
    instance = foo_mock.return_value
    instance.echo.return_value = 'mock result'
    result = some_function()
    assert result == 'mock result'


if __name__ == '__main__':
    foo = Foo()
    foo.echo = mock.MagicMock()
    foo.echo.return_value = 'mock value'

    print some_function()



