from abc import ABC, abstractmethod

# Interface I1
class I1(ABC):
    @abstractmethod
    def fun1(self):
        pass

    @abstractmethod
    def fun(self):
        pass

# Interface I2
class I2(ABC):
    @abstractmethod
    def fun2(self):
        pass

    @abstractmethod
    def fun(self):
        pass

# Interface I extending both I1 and I2
class I(I1, I2):
    pass

# Class C implementing interface I
class C(I):
    def fun1(self):
        print("C: fun1() called")

    def fun2(self):
        print("C: fun2() called")

    def fun(self):
        print("C: fun() called")

# Unit tests
import unittest

class TestInterfaces(unittest.TestCase):
    def test_interface_inheritance(self):
        obj = C()
        self.assertTrue(isinstance(obj, I1))
        self.assertTrue(isinstance(obj, I2))
        self.assertTrue(isinstance(obj, I))

        self.assertTrue(hasattr(obj, 'fun1'))
        self.assertTrue(hasattr(obj, 'fun2'))
        self.assertTrue(hasattr(obj, 'fun'))

        obj.fun1()
        obj.fun2()
        obj.fun()

if __name__ == '__main__':
    unittest.main()
