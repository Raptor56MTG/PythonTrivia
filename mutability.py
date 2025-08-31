test1 = 200
test2 = 1_000_000

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

def prerequisite3():
    # Case 1: literals in the same code block
    a = 1000
    b = 1000
    print("Case 1: literals")
    print("a == b:", a == b)     # True → same value
    print("a is b:", a is b)     # True in most scripts → same object
    print("id(a):", id(a))
    print("id(b):", id(b))
    print()

    # Case 2: dynamically created integers
    x = int('1000')
    y = int('1000')
    print("Case 2: dynamically created")
    print("x == y:", x == y)     # True → same value
    print("x is y:", x is y)     # False → different objects
    print("id(x):", id(x))
    print("id(y):", id(y))
    print()

        # Case 2: dynamically created integers
    i = int('100')
    j = int('100')
    print("Case 2: dynamically created")
    print("i == j:", i == j)     # True → same value
    print("i is j:", i is j)     # False → different objects
    print("id(i):", id(i))
    print("id(j):", id(j))
    print()

    # Case 3: computed at runtime
    m = 500 + 500
    n = 1000
    print("Case 3: runtime computation")
    print("m == n:", m == n)     # True → same value
    print("m is n:", m is n)     # Usually False → different objects
    print("id(m):", id(m))
    print("id(n):", id(n))

    # Case 4: computed at runtime
    c = 100 + 100
    d = 200
    print("Case 3: runtime computation")
    print("c == d:", c == d)     # True → same value
    print("c is d:", c is d)     # Usually False → different objects
    print("id(c):", id(c))
    print("id(d):", id(d))

def prerequisite4():
    a = []
    b = a
    b.append(1)
    print(a, id(a))  # id is the memory address
    print(b, id(b))  # id is the memory address

def questions():
    """
    1. Why do A and C have the same address in memory?

    2. Why Does C's memory Address change?

    3. Why Do C and B have the same address in memory?

    4. Is there a way to guarantee the same address or not?
    """
    pass

def takeaways():
    """
    Everything in python is an object.
    for non mutable integers, you can only assume the ID's will match for those that are in
    the cached range. Outside of that there is no guarantee.
    """

def problem1():
    grid = ["0"] * 3
    print(grid)
    grid[0] = 3
    print(grid)

def problem2():
    grid = [[0]] * 3
    print(grid)
    grid[0] = 3
    print(grid)

def problem3():
    grid = [[0, 0, 0]] * 3
    print(grid)
    grid[0][0] = 3
    print(grid)

def problem4():
    a = 5
    grid = [a] * 3
    print(grid)
    grid[0] += 1
    print(grid)

if __name__ == '__main__':
    # prerequisite1()
    # prerequisite2()
    # prerequisite3()
    # prerequisite4()
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    pass

def explanation():
    """
    When we use * 3 on a list, it does not create a new list. Rather, it copies the reference to that list.
    We end up with a list that has three pointers to the same object, so when that object is modified, all three
    pointers end up pointing to the same modified object.

    In python, it is best to be EXPLICIT rather than IMPLICIT.

    * with mutable objects replicates references, not the objects themselves.
    * With immutable objects, its safe — each “copy” behaves independently.
    """
    pass