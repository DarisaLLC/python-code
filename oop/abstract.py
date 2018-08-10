from abc import ABC, abstractmethod

"""
Abstract classes contain one or more abstract method, which are declared but
require an implementation in a derived class. An abstract class itself is not
instantiable.
"""

class NotAbstract:

    def foo(self):
        pass

class ConcreteChild(NotAbstract):
    pass

"""
Notice that the Python language doesn't provide any notion of abstract classes.
However, the standard library provides the abc package which can simulate abc's.
"""
a = NotAbstract()
b = ConcreteChild()

class AbstractAdd(ABC):

    def __init__(self, x):
        super().__init__()
        self.x = x

    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        return 25

class Add42(AbstractAdd):

    def foo(self):
        return self.x + 42

    # notice that a method with the @abstractmethod decorator may have a body in
    # the abstract class, but still needs to be overridden, the parent
    # implementation can still be called via the super() proxy object
    def bar(self):
        return super().bar()

# if Add42 doesn't implement the abstract method, we get
# TypeError: Can't instantiate abstract class Add42 with abstract methods foo
c = Add42(10)
print(c.foo())
