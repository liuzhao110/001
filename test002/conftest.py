__author__ = 'liusir'
#coding: utf-8

#from test_foocompare import Foo
import pytest

@pytest.fixture()
def login():
    print ('输入账号、密码登录')