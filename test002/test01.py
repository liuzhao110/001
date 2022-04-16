import pytest

@pytest.fixture()
def before():
    print('\nBefore each test')

def test_1(before):
    print ('test_1()')

def test_2(before):
    print ('test_2()')
    assert 0    # For test purpose

if __name__ == "__main__":
    pytest.main(["-v", "-s", "test01.py"])