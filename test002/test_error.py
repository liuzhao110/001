__author__ = 'liusir'
# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 17:34
# @Author  : longrong.lang
# @FileName: test_error.py
# @Software: PyCharm
# @Cnblogs ：https://www.cnblogs.com/longronglang
'''
代码编写上的错误栗子
'''
import pytest


@pytest.fixture()
def data():
    str = 'python'
    assert 'test' in str
    return str


def test_error(data):
    assert data == 'python'


if __name__ == '__main__':
    pytest.main(["-q", "test_error.py"])
