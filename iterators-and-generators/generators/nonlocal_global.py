# global refers to a global variable in an enclosing scope
def outer(): 
    s = "out"
    def inner():
        # non local refers to variable in an enclosing function scope
        # it was introduced to make functon nesting easier
        nonlocal s 
        s = "in" 
        print(s)
    inner()
    print(s)

outer()
