__author__ = 'liusir'
import pytest

@pytest.fixture()
def before():
    print ('\nBefore each test')

@pytest.mark.usefixtures("before")
def test_1():
    print('test_1()')

@pytest.mark.usefixtures("before")
def test_2():
    print ('test_2()')

class Test1:
    @pytest.mark.usefixtures("before")
    def test_3(self):
        print ('test_3()')

    @pytest.mark.usefixtures("before")
    def test_4(self):
        print ('test_4()')

@pytest.mark.usefixtures("before")
class Test2:
    def test_5(self):
        print ('test_5()')

    def test_6(self):
        print ('test_6()')

if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_module.py"])