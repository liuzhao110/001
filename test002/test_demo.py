__author__ = 'liusir'
# encoding utf-8
# content of test_demo.py
import pytest
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5

class TestDemo:
      def test_a(self):
          print("a")
      def test_b(self):
         print("b")
      def c(self):
         print("c")

if __name__=="__main__":
    pytest.main(['-v','-s','test_demo.py'])