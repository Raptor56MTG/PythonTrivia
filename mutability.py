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
    a += 1
    print(grid)
    print(a)


if __name__ == '__main__':
    problem1()
    problem2()
    problem3()
    problem4()
    pass

def explanation():
    """
    When we use * 3 on a list, it does not create a new list. Rather, it copies the reference to that list.
    We end up with a list that has three pointers to the same object, so when that object is modified, all three
    pointers end up pointing to the same modified object.

    In python, it is best to be EXPLICIT rather than IMPLICIT.

    * with mutable objects, we replicate references, not the objects themselves.
    * With immutable objects, its safe — each “copy” behaves independently.
    """
    pass