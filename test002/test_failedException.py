__author__ = 'liusir'
# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 17:26
# @Author  : longrong.lang
# @FileName: test_failedException.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
'''
断言失败的栗子
'''
import pytest


@pytest.fixture()
def data():
    return 'python'


def test_failed(data):
    # 这块随便抛出一个异常了
    raise IOError
    assert 'py' in data


if __name__ == '__main__':
    pytest.main(["-q", "test_failedException.py"])
