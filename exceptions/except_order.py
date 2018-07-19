class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        # raise allows the program to force a specific exception to occur
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    # an except clause may associate a variable name with an instance of the exception
    # the instance will have __str__ defined, allowing printing the exception message
    except B as b:
        print("B")

        # when an exception should not be handled, it can be raised again
        # raise
    # be careful because this may hide real programming errors
    except:
        print("Excluding the exception name in the last except clause serves as a wildcard.")
