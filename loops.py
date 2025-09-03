def helpful_context():
    """This part primarily focuses on your understanding of loops.
    What is going on in a for loop in python under the hood?"""

def problem1():
    for x in range(3):
        print(x)
        x = 3

def problem2():
    x = 0
    while x < 3:
        print(x)
        x = 3

if __name__ == '__main__':
    # problem1()
    problem2()

def explanation():
    """
    In order to understand this problem, you need to know how for loops work under the hood.
    In python, for loops are actually a combination of iterables and iterators.

    Iterable: Something that can be iterated over.

    Examples:
        - list
        - string
        - tuple

    Iterators: Something that can iterate over an object.

    What this means is that a for loop is actually doing the following under the hood.

    my_list = [1, 2, 3]
    for item in my_list:
        print(item)
    
    iter(my_list)
    next(my_list)
    next(my_list)
    next(my_list)
    next(my_list) # raises StopIteration exception

    For loops in python handle StopIteration errors for us gracefully, we never have to deal with them.

    What this is telling us then, is that our assignment to x never actually does anything, as it has no
    real effect on the iterator under the hood.

    This is why in other languages, the more intuitive outcome would occur. Those for loops are index based,
    where as pythons are iterator based.

    Good resource: https://www.youtube.com/watch?v=JHB0cbsmPoM

    """
    pass