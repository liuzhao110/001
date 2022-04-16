__author__ = 'liusir'

#coding: utf-8

import pytest

@pytest.fixture()
#def login():
   # print ('输入账号、密码登录')

def test_step_1(login):
    print ('用例步骤1：登录之后其它动作111')

def test_step_2(): #不需要登录
    print ('用例步骤2: 不需要登录， 操作222')

def test_step_3(login):
    print ('用例步骤3：登录之后其它动作333')

if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_smtp01.py"])