def helpful_context():
    """This problem focuses on scoping in python."""
    pass

a = 1
b = 2
c = 3

def problem3():
    print(a)
    b += 1
    print(b)


def problem4():
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


if __name__ == '__main__':
    problem3()
    # problem4()