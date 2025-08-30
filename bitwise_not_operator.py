def helpful_context():

    """
    TOPIC: Bitwise Not operator

    What does ~ mean?
    
    ~ before a number indicates the bitwise NOT operator. It functions like this.
    
    ~i -> (i + 1) * -1
    examples: 

    ~5 => -6
    ~0 => -1
    """
    pass


def problem1():
    size = 5
    foo = list(range(size))
    if foo[2] != foo[~2]:
        print("Invalid Comparison!")
    size = 10
    bar = list(range(size))
    if bar[~2] % 2 == 0:
        print("Bad modular arithmetic.")
    else:
        print("All Valid!")


def problem2():
    foo = [1, 2, 3, 4, 5]
    for i in range(sum(divmod(len(foo), 2))):
        print(foo[i], foo[~i], sep="", end="")


if __name__ == '__main__':
    problem1()
    # problem2()
