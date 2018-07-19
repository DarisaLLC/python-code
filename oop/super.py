# super() enables a derived class to accses inherited methods which it has
# overridden, and to access a base class without knowing its name
# note in Python the base constructor is not called if the derived classs has
# its own
#
# Python3
# super().methoName(args)
#
# Python2
# super(subClass, instance).method(args)

class Base:
    def __init__(self):
        print("Base constructor")

class Derived(Base):
    def __init__(self):
        # specify base class
        Base.__init__(self)

        # python2 super
        super(Derived, self).__init__()

        # python3 super
        super().__init__()

        # returns a proxy object
        print(type(super()))

        print("Derived constructor")

d = Derived()
