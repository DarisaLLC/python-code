class Base:

    static_x = 1

    def __init__(self, instance_x):
        self.instance_x = instance_x

    def greeting(self):
        print(Base.static_x, self.static_x)
        print(self.instance_x)

class Derived(Base):

    static_y = 3

    def __init__(self, instance_y):
        self.instance_y = instance_y

    def greeting(self):
        print(Derived.static_y, self.static_y)
        print(self.instance_y)

        print(Derived.static_x, self.static_x)
        print(self.static_x)

if __name__ == "__main__":

    b = Base(2)
    b.greeting()

    d = Derived(4)
    d.greeting()
