def problem():
    difficulties = [
            'easy',  # <---- comma
            'medium' # <---- no comma
            'hard' # <------- no comma
        ]
    print(difficulties)

if __name__ == '__main__':
    problem()

def explanation():
    """
    This one is pretty simple. There are two rules that define this in the python documentation.

    1. "A logical line is constructed from one or more physical lines by following explicit or
    implicit line joining rules."   

    2. "Expressions in parentheses, square brackets, or curly braces can be split over more
    than one physical line without using backslashes."

    There are two ways to fix this. 
    
    The first is to add a comma. The second is to add a trailing or hanging comma. This can prevent
    possible bugs. A great example of this can be seen in our config file in django. I believe we did
    have something similar to this occur way back in the day.

    This was also the bug that caused me to break LIMS for the first time. I had a list of tuples
    and forgot to add a comma.

    It is important to note that not all languages
    or formats allow for dangling commas. JSON is a great example where this is not allowed.
    """
    pass

def fix():
    difficulties = [
            'easy',  # <---- comma
            'medium', # <---- comma
            'hard' # <------- no comma
        ]
    print(difficulties)

def better_fix():
    difficulties = [
            'easy',  # <---- comma
            'medium', # <---- comma
            'hard', # <------- no comma
        ]
    print(difficulties)
