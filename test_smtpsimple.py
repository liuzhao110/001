__author__ = 'liusir'
import pytest
import time

#@pytest.fixture(scope="module")
@pytest.fixture(scope="module",autouse=True)
def mod_header(request):
    print ('\n------------------')
    print ('module   : %s' % request.module.__name__)
    print ('-------------------')

#@pytest.fixture(scope="function")
@pytest.fixture(scope="function",autouse=True)
def func_header(request):
    print ('\n------------------')
    print ('function:    %s' % request.module.__name__)
    print ('time:        %s' % time.asctime())
    print ('-------------------')

def test_1(mod_header,func_header):
    print ('in test_1()')

def test_2(mod_header,func_header):
    print ('in test_2()')

if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_smtpsimple.py"])