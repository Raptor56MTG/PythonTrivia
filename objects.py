def prerequisite1():
    a = 1
    b = a
    b += 1
    print(a, id(a))
    print(b, id(b))
    print(a is b)

def prerequisite2():
    c = 1
    print(c, id(c))
    c += 1
    print(c, id(c))

def javan_test():
    a = 10000
    c = 10000
    print(a, c, id(a), id(c))


def questions():
    """
    1. Why do A and C have the same address in memory?

    2. Why Does C's memory Address change?

    3. Why Do C and B have the same address in memory?

    4. Is there a way to guarantee the same address or not?
    """
    pass

def prerequisite3():
    # Case 1: literals in the same code block
    a = 1000
    b = 1000
    print("a, b", a, b)
    print("Case 1: literals")
    print("a == b:", a == b) # True --> same value
    print("a is b:", a is b) # True in most scripts --> same object
    print("id(a):", id(a))
    print("id(b):", id(b))
    print()

    # Case 2: dynamically created integers
    x = int('1000')
    y = int('1000')
    print("x, y", x, y)
    print("Case 2: dynamically created")
    print("x == y:", x == y) # True --> same value
    print("x is y:", x is y) # False --> different objects
    print("id(x):", id(x))
    print("id(y):", id(y))
    print()

    # Case 2: dynamically created integers
    i = int('100')
    j = int('100')
    print("Case 2: dynamically created")
    print("i, j", i, j)
    print("i == j:", i == j) # True --> same value
    print("i is j:", i is j) # True (in range of cached values)
    print("id(i):", id(i))
    print("id(j):", id(j))
    print()

    # Case 3: computed at runtime
    m = 500 + 500
    n = 1000
    print("Case 3: runtime computation")
    print("m, n", m, n)
    print("m == n:", m == n) # True --> same value
    print("m is n:", m is n) # Usually False --> different objects
    print("id(m):", id(m))
    print("id(n):", id(n))

    # Case 4: computed at runtime
    c = 100 + 100
    d = 200
    print("Case 4: runtime computation")
    print("c, d", c, d)
    print("c == d:", c == d) # True --> same value
    print("c is d:", c is d) # True --> (in range of cached values)
    print("id(c):", id(c))
    print("id(d):", id(d))

def prerequisite4():
    a = []
    b = a
    b.append(1)
    print(a, id(a))  # id is the memory address
    print(b, id(b))  # id is the memory address


def julian_test():
    a = "hello world"
    b = a
    print(a, id(a))
    print(b, id(b))

if __name__ == '__main__':
    # javan_test()
    # prerequisite1()
    # prerequisite2()
    # prerequisite3()
    # prerequisite4()
    julian_test()
    pass

def takeaways():
    """
    https://jakevdp.github.io/PythonDataScienceHandbook/02.01-understanding-data-types.html

    Everything in python is an object.
    for non mutable integers, you can only assume the ID's will match for those that are in
    the cached range. Outside of that there is no guarantee.

    References and mutability
    * with mutable objects, we replicate references, not the objects themselves.
    * With immutable objects, its safe — each “copy” behaves independently.
    """
    pass