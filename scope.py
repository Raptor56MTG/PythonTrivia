def helpful_context():
    """This problem focuses on your understanding of the LEGB scope in python."""
    pass

a = 1
b = 2
c = 3

def problem1():
    print(a)
    b += 1
    print(b)


def problem2():
    a = 4
    b = 5
    def inner():
        nonlocal a
        global b
        print(a, end  = ", ")
        print(b, end = ", ")
        print(c)
        a = 6
        b = 7
        c = 8
    inner()


def problem3():
    a = 6
    b = 7
    def inner():
        nonlocal a
        a += 4
        print(a, end  = ", ")
        print(b, end = ", ")
    inner()


if __name__ == '__main__':
    # problem1()
    problem2()
    # problem3()


def explanation():
    """
    This comes down to understanding scoping in python. When python looks for variables, it uses the following approach.

    LEGB

    L - Looks for the LOCAL instance.
    E - Looks for the ENCLOSED instance.
    G - Looks for the GLOBAL instance.
    B - Looks for the BUILT IN instance. (these are built in functions.)

    https://realpython.com/python-scope-legb-rule/
    
    
    In our first problem, we are actually able to print a despite not defining it locally because it
    was able to find it by going down the LEBG path. The second step fails because when we see b += 1,
    that is the same as b = b + 1 and python assumes this is a local variable assignment, causing it to fail.
    
    In our second problem, we use terms like global and non local to reference global and enclosed instances
    and modify them as needed. These work as intended. C fails because we are assigning to it, which causes our
    code to view it as a local variable. Python then sees this as us accessing a local variable before instantiation.

    The third problem is just a way to test our understanding of the LEGB path.

    """
    pass        
